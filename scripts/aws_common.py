import datetime
import json
from pathlib import Path
from typing import Optional

import boto3

THIS_DIR = Path(__file__).parent
BUILD_DIR = THIS_DIR.parent / "build"


class CredentialCache(object):
    def __init__(self, profile: Optional[str] = None, mfa: Optional[str] = None):
        cached_creds = CachedCredentials()
        if cached_creds.valid():
            self.session = cached_creds.session()
            return

        session = boto3.Session(
            profile_name=profile
        )

        if mfa is not None:
            sts = session.client("sts")
            mfa_code = input("Input your MFA code: ").strip()
            response = sts.get_session_token(
                DurationSeconds=60 * 60,
                SerialNumber=mfa,
                TokenCode=mfa_code
            )
            creds = response['Credentials']
            cached_creds.cache(creds)
            self.session = cached_creds.session()


class CachedCredentials(object):
    def __init__(self):
        creds_file = BUILD_DIR / "cache/aws/creds.json"
        self.access_key_id = None
        if not creds_file.exists():
            return

        with creds_file.open("rt", encoding='utf-8') as f:
            self.cache(json.load(f))

    def valid(self) -> bool:
        return self.access_key_id is not None

    def cache(self, data):
        expiration = data['Expiration']
        if isinstance(expiration, datetime.datetime):
            data['Expiration'] = expiration.isoformat()
        elif isinstance(expiration, str):
            expiration = datetime.datetime.fromisoformat(expiration)

        now_utc = datetime.datetime.utcnow()

        delta = expiration.replace(tzinfo=None) - now_utc

        # if session token validity < 60 sec, reject it
        if delta.total_seconds() < 60:
            return

        creds_file = BUILD_DIR / "cache/aws/creds.json"
        if not creds_file.parent.exists():
            creds_file.parent.mkdir(parents=True)

        with creds_file.open("wt", encoding='utf-8') as of:
            json.dump(data, of)
            of.flush()

        self.access_key_id = data['AccessKeyId']
        self.secret_access_key = data['SecretAccessKey']
        self.session_token = data['SessionToken']

    def session(self):
        return boto3.Session(
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key,
            aws_session_token=self.session_token
        )


if __name__ == '__main__':
    import sys

    cache = CredentialCache(sys.argv[1], sys.argv[2])
