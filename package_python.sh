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

if [ -z "$NO_WHEELS" ] && [ ! -d "$BINARY_DIC_ROOT" ]; then
  echo "binary dictionaries are not present in $BINARY_DIC_ROOT"
  echo "run ./gradlew build to compile binary dictionaries"
  exit 1
fi

set +e
rm -rf "$PACKAGES_ROOT/$VERSION"
if [ -z "$NO_WHEELS" ]; then
  mkdir -p "$PACKAGES_ROOT/wheels"
fi
mkdir -p "$PACKAGES_ROOT/sdist"

set -e
home=$SCRIPT_DIR
for dict_type in small core full
do
    temp="$PACKAGES_ROOT/$VERSION/$dict_type"
    pkg="${temp}/sudachidict_${dict_type}"
    mkdir -p ${pkg}
    # prepare package directory
    mkdir "${pkg}/resources"
    touch "${pkg}/__init__.py"
    cp python/README.md "${temp}"
    cp LEGAL ${temp}
    cp LICENSE-2.0.txt "${temp}"
    cp python/MANIFEST.in "${temp}"
    cp python/setup.py "${temp}"
    cat python/INFO.json | sed "s/%%VERSION%%/${VERSION}/g" | sed "s/%%DICT_VERSION%%/${DICT_VERSION}/g" | sed "s/%%DICT_TYPE%%/${dict_type}/g" > ${temp}/INFO.json

    if [ -z "$NO_WHEELS" ]; then
      # build a wheel with binary dictionaries included
      cp "$BINARY_DIC_ROOT/system_${dict_type}.dic" "${pkg}/resources/system.dic"
      python3 -m build \
        --outdir "$PACKAGES_ROOT/wheels" \
        --no-isolation --wheel \
        "${temp}"
    fi

    # build sdist with binary dictionary not included
    rm -rf "${pkg}/resources"
    python3 -m build \
      --outdir "$PACKAGES_ROOT/sdist" \
      --no-isolation --sdist \
      "${temp}"
done
