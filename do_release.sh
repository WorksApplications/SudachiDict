#!/usr/bin/env bash

# This is a script for doing a SIMPLE release
# How to run: do_release.sh DICT_VERSION /path/to/directory/with/raw/dictionaries aws_profile aws_mfa_uid
# You also need to have prepared python virtual environment with dependencies
# See RELEASE.md for details

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

DICT_VERSION=$1
RAW_DIC_PATH=$2
AWS_PROFILE=$3
AWS_MFA_ID=$4
if [ -z "$5" ]; then
  PY_PACKAGE_VERSION=${DICT_VERSION}
else
  PY_PACKAGE_VERSION=$5
fi

# upload dictionary csvs to s3
python3 "$SCRIPT_DIR/scripts/01_upload_raw_dictionaries.py" \
  --input="$RAW_DIC_PATH" \
  --version="$DICT_VERSION" \
  --aws_profile="$AWS_PROFILE" \
  --aws_mfa="$AWS_MFA_ID"

# build binary dictionaries
"$SCRIPT_DIR/gradlew" -Pdict.release=true -Pdict.version="$DICT_VERSION" build

# upload binary dictionaries to s3
python3 "$SCRIPT_DIR/scripts/02_upload_compiled_dictionaries.py" \
  --input="$SCRIPT_DIR/build/distributions" \
  --aws_profile="$AWS_PROFILE" \
  --aws_mfa="$AWS_MFA_ID"

# build python distributions
bash $SCRIPT_DIR/package_python.sh "$DICT_VERSION" "$PY_PACKAGE_VERSION"
