#!/bin/bash
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# guess versions
if [ -z "$1" ]; then
    DICT_VERSION=$("$SCRIPT_DIR/gradlew" -q showVersion)
    VERSION=${DICT_VERSION}
else
    DICT_VERSION=$1
    if [ -z "$2" ]; then
        VERSION=${DICT_VERSION}
    else
        VERSION=$2
    fi
fi

echo "VERSION=$VERSION, DICT_VERSION=$DICT_VERSION"

PACKAGES_ROOT="$SCRIPT_DIR/build/python"
BINARY_DIC_ROOT="$SCRIPT_DIR/build/dict/bin/$DICT_VERSION"

if [ ! -d "$BINARY_DIC_ROOT" ]; then
  echo "binary dictionaries are not present in $BINARY_DIC_ROOT"
  echo "run ./gradlew build to compile binary dictionaries"
  exit 1
fi

set +e
rm -rf "$PACKAGES_ROOT/$VERSION"
WHEELS_DIR="$PACKAGES_ROOT/wheels"
mkdir -p "$WHEELS_DIR"

set -e
home=$SCRIPT_DIR
for dict_type in small core full
do
    temp="$PACKAGES_ROOT/$VERSION/$dict_type"
    pkg="${temp}/sudachidict_${dict_type}"
    mkdir -p ${pkg}
    mkdir ${pkg}/resources
    touch ${pkg}/__init__.py
    cp python/README.md ${temp}
    cp LEGAL ${temp}
    cp LICENSE-2.0.txt ${temp}
    cp python/MANIFEST.in ${temp}
    cp python/setup.py ${temp}
    cat python/INFO.json | sed "s/%%VERSION%%/${VERSION}/g" | sed "s/%%DICT_VERSION%%/${DICT_VERSION}/g" | sed "s/%%DICT_TYPE%%/${dict_type}/g" > ${temp}/INFO.json
    cp "$BINARY_DIC_ROOT/system_${dict_type}.dic" "${temp}/sudachidict_${dict_type}/resources/system.dic"
    pip wheel \
      --wheel-dir "$WHEELS_DIR" \
      --no-deps --no-build-isolation \
      "${temp}"
    # python setup.py bdist_wheel sdist
done
