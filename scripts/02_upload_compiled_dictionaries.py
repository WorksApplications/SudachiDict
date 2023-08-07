import re
from pathlib import Path

from classopt import classopt, config

from aws_common import CredentialCache


@classopt(default_long=True)
class Opts:
    input: Path
    aws_profile: str = None
    aws_mfa: str = None
    aws_region: str = "ap-northeast-1"
    s3_bucket: str = "sudachi"
    s3_prefix: str = "sudachidict"
    no_latest: bool = config(action='store_true')


BINARY_DIC_PATTERN = re.compile("^sudachi-dictionary-.*-(small|core|full).zip$")


def make_latest_name(name: str) -> str:
    m = BINARY_DIC_PATTERN.match(name)
    kind = m.group(1)
    return f"sudachi-dictionary-latest-{kind}.zip"


def prepare_files(args: Opts) -> list[Path]:
    result = []

    for child in args.input.iterdir():
        if child.is_file() and BINARY_DIC_PATTERN.match(child.name) is not None:
            result.append(child)

    return result


def upload_files(s3, args: Opts, files: list[Path]):
    bucket = s3.Bucket(args.s3_bucket)
    for file in files:
        s3_key = f"{args.s3_prefix}/{file.name}"
        with file.open('rb') as f:
            resp = bucket.put_object(
                Body=f,
                Key=s3_key,
                ContentType='application/zip'
            )
            print("put", file, "size", resp.content_length, "to", s3_key, "etag", resp.e_tag)

            if not args.no_latest:
                latest_name = make_latest_name(file.name)
                latest_s3_key = f"{args.s3_prefix}/{latest_name}"
                bucket.put_object(
                    Body=b"",
                    Key=latest_s3_key,
                    WebsiteRedirectLocation="/" + s3_key
                )
                print("set", latest_s3_key, "redirect to", s3_key)


def main(opts: Opts):
    session = CredentialCache(opts.aws_profile, opts.aws_mfa).session
    files = prepare_files(opts)
    s3 = session.resource("s3")
    upload_files(s3, opts, files)


if __name__ == '__main__':
    main(Opts.from_args())
