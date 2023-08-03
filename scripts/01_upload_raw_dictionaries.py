from pathlib import Path

from classopt import classopt

from aws_common import CredentialCache
from raw_listing import generate_raw_listing


@classopt(default_long=True)
class Opts:
    input: Path
    version: str
    aws_profile: str
    aws_mfa: str
    aws_region: str = "ap-northeast-1"
    s3_bucket: str = "sudachi"
    s3_prefix: str = "sudachidict-raw"


def validate_file(file: Path) -> Path:
    if file.exists():
        return file
    raise FileNotFoundError(f"required file {file} was not present")


def validate_files(args: Opts) -> list[Path]:
    return [
        validate_file(args.input / "small_lex.zip"),
        validate_file(args.input / "core_lex.zip"),
        validate_file(args.input / "notcore_lex.zip"),
    ]


def make_client(args):
    return CredentialCache(args.aws_profile, args.aws_mfa).session.resource("s3", region_name=args.aws_region)


def upload_files(client, args: Opts, files: list[Path]):
    bucket = client.Bucket(args.s3_bucket)
    for file in files:
        s3_key = f"{args.s3_prefix}/{args.version}/{file.name}"
        with file.open('rb') as f:
            resp = bucket.put_object(
                Body=f,
                Key=s3_key,
                ContentType='application/zip'
            )
            print("put", file, "size", resp.content_length, "to", s3_key, "etag", resp.e_tag)


def regenerate_index(s3, args: Opts):
    listing = generate_raw_listing(s3, args.s3_bucket, args.s3_prefix)
    bucket = s3.Bucket(args.s3_bucket)

    bucket.put_object(
        Body=listing.encode("utf-8"),
        Key=f"{args.s3_prefix}/index.html",
        ContentType="text/html; charset=utf-8",
    )
    print("updated index.html")


def main(args: Opts):
    files = validate_files(args)
    client = make_client(args)
    upload_files(client, args, files)
    regenerate_index(client, args)


if __name__ == '__main__':
    main(Opts.from_args())
