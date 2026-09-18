# Copyright (c) 2020-2026 Works Applications Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools
import os
import json
import sys
from urllib.parse import urlparse
from urllib.request import urlretrieve
from zipfile import ZipFile

with open("INFO.json", encoding="utf-8") as fh:
    dict_info = json.load(fh)
PKG_VERSION = dict_info["version"]
DICT_VERSION = dict_info["dict_version"]
DICT_EDITION = dict_info["edition"]
DICT_FORMAT = dict_info.get("dictionary_format", "v0")

BASE_URL = "https://d2ej7fkh96fzlu.cloudfront.net/sudachidict"
if DICT_FORMAT == "v1":
    BASE_URL += "/v1"
else: # v0
    BASE_URL += "/v0"
ZIP_URL = f"{BASE_URL}/sudachi-dictionary-{DICT_VERSION}-{DICT_EDITION}.zip"
ZIP_NAME = urlparse(ZIP_URL).path.split("/")[-1]
UNZIP_NAME = f"sudachi-dictionary-{DICT_VERSION}"
PKG_DIR = f"sudachidict_{DICT_EDITION}"
RESOURCE_DIR = os.path.join(PKG_DIR, "resources")
BINARY_NAME = f"system_{DICT_EDITION}.dic"

# Download and place the dictionary file
if not os.path.exists(RESOURCE_DIR):
    print("Downloading the binary Sudachi dictionary (it may take some time) ...", file=sys.stderr)
    _, _msg = urlretrieve(ZIP_URL, ZIP_NAME)
    with ZipFile(ZIP_NAME) as z:
        z.extractall()
    os.rename(UNZIP_NAME, RESOURCE_DIR)
    os.rename(os.path.join(RESOURCE_DIR, BINARY_NAME),
              os.path.join(RESOURCE_DIR, "system.dic"))
    os.remove(ZIP_NAME)
    print(f"downloaded and extracted dictionary to `{RESOURCE_DIR}`.", file=sys.stderr)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=f"SudachiDict-{DICT_EDITION}",
    version=PKG_VERSION,
    description=f"Sudachi Dictionary for SudachiPy - {DICT_EDITION.title()} Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WorksApplications/SudachiDict",
    license="Apache-2.0",
    author="Works Applications",
    author_email="sudachi@worksap.co.jp",
    packages=setuptools.find_packages(),
    package_data={"": ["resources/*"]},
    install_requires=[
        "SudachiPy>=0.7.0,<2.0" if DICT_FORMAT == "v1" else "SudachiPy>=0.5,<0.7"
    ],
)
