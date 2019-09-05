#!/bin/bash
set -e
version=`grep -oP -m 1 '<version>\K([^<]+)' pom.xml`

set +e
rm -r target/python/${version}

set -e
home=`pwd`
for dic_type in small core full
do
    temp=target/python/${version}/${dic_type}
    pkg=${temp}/sudachidict_${dic_type}
    mkdir -p ${pkg}/resources/
    touch ${pkg}/__init__.py
    cp target/system_${dic_type}.dic ${pkg}/resources/system.dic
    cp README.md ${temp}
    cp LEGAL ${temp}
    cp LICENSE-2.0.txt ${temp}
    cp MANIFEST.in ${temp}
    cat setup.py.template | sed "s/%%VERSION%%/${version}/g" | sed "s/%%DIC_TYPE%%/${dic_type}/g" > ${temp}/setup.py
    cd ${temp}
    python setup.py sdist
    cp dist/*.tar.gz ${home}/target/
    cd ${home}
    rm -r ${temp}
done
rm -r target/python/${version}
