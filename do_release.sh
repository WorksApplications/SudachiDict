#!/usr/bin/env bash

# This is a script for doing a SIMPLE release
# You need to have prepared python virtual environment with dependencies
# See RELEASE.md for details
# 
# How to run:
#   `do_release.sh <FORMAT_VERSION> <DICT_VERSION> </path/to/directory/with/raw/dictionaries> <aws_profile> <aws_mfa_uid> [<DICT_VERSION_FOR_PYTHON>]`
#     e.g. `do_release.sh v0 20260723 ./raw_dict/20260723/v0/ aws_profile arn:aws:iam::0123456789012:mfa/hoge-fuga`

set -euox pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ $# -ne 5 ] && [ $# -ne 6 ]; then
    >&2 echo "Usage: $0 <FORMAT_VERSION> <DICT_VERSION> <RAW_DIC_PATH> <AWS_PROFILE> <AWS_MFA_ID> [<PY_PACKAGE_VERSION>]"
    >&2 echo "Example: $0 v0 20260723 ./raw_dict/20260723/v0/ aws_profile arn:aws:iam::0123456789012:mfa/hoge-fuga"
    exit 1
fi

FORMAT_VERSION=$1; shift
DICT_VERSION=$1; shift
RAW_DIC_PATH=$1; shift
AWS_PROFILE=$1; shift
AWS_MFA_ID=$1; shift
if [ $# -eq 0 ]; then
  PY_PACKAGE_VERSION=${DICT_VERSION}
else
  PY_PACKAGE_VERSION=$1; shift
fi

# arg validation
if [ $FORMAT_VERSION != "v0" ] && [ $FORMAT_VERSION != "v1" ]; then
  >&2 echo "Unsupported dictionary format version: $FORMAT_VERSION"
  exit 1
fi

# upload dictionary csvs to s3
python3 "$SCRIPT_DIR/scripts/01_upload_raw_dictionaries.py" \
  --input="$RAW_DIC_PATH" \
  --version="$DICT_VERSION" \
  --aws_profile="$AWS_PROFILE" \
  --aws_mfa="$AWS_MFA_ID" \
  --dictionary_format "$FORMAT_VERSION"

# build binary dictionaries
if [ "$FORMAT_VERSION" = "v0" ]; then
  RELEASE_FLAG="true"
else # v1
  RELEASE_FLAG="false"
fi

"$SCRIPT_DIR/gradlew" -Pdict.release=$RELEASE_FLAG -Pdict.format="$FORMAT_VERSION" -Pdict.version="$DICT_VERSION" build

# upload binary dictionaries to s3
python3 "$SCRIPT_DIR/scripts/02_upload_compiled_dictionaries.py" \
  --input="$SCRIPT_DIR/build/distributions/$FORMAT_VERSION" \
  --version="$DICT_VERSION" \
  --aws_profile="$AWS_PROFILE" \
  --aws_mfa="$AWS_MFA_ID" \
  --dictionary_format "$FORMAT_VERSION"

# build python distributions
if [ "$FORMAT_VERSION" = "v0" ]; then
  bash $SCRIPT_DIR/package_python.sh "$DICT_VERSION" "$PY_PACKAGE_VERSION"
else # v1
  >&2 echo "We only kick python packaging for dictionary format version V0."
fi
