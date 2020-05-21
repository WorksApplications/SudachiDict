#!/bin/bash
set -e
version=`grep -oP -m 1 '<version>\K([^<]+)' pom.xml`

set +e
rm -rf target/python/${version}

set -e
home=`pwd`
for dict_type in small core full
do
    temp=target/python/${version}/${dict_type}
    pkg=${temp}/sudachidict_${dict_type}
    mkdir -p ${pkg}
    touch ${pkg}/__init__.py
    cp python/README.md ${temp}
    cp LEGAL ${temp}
    cp LICENSE-2.0.txt ${temp}
    cp python/MANIFEST.in ${temp}
    cp python/setup.py ${temp}
    cat python/INFO.json | sed "s/%%VERSION%%/${version}/g" | sed "s/%%DICT_TYPE%%/${dict_type}/g" > ${temp}/INFO.json
    cd ${temp}
    python setup.py sdist
    cp dist/*.tar.* ${home}/target/
    cd ${home}
    rm -r ${temp}
done
rm -r target/python/${version}
