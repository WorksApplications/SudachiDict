# Copyright (c) 2020 Works Applications Co., Ltd.
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
from logging import getLogger
from urllib.parse import urlparse
from urllib.request import urlretrieve
from zipfile import ZipFile


with open("INFO.json") as fh:
    dict_info = json.load(fh)
PKG_VERSION = dict_info["version"]
DICT_VERSION = dict_info["dict_version"]
DICT_EDITION = dict_info["edition"]

ZIP_URL = "http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/"\
          "sudachi-dictionary-{}-{}.zip".format(DICT_VERSION, DICT_EDITION)
ZIP_NAME = urlparse(ZIP_URL).path.split("/")[-1]
UNZIP_NAME = "sudachi-dictionary-{}".format(DICT_VERSION)
PKG_DIR = "sudachidict_{}".format(DICT_EDITION)
RESOURCE_DIR = os.path.join(PKG_DIR, "resources")
BINARY_NAME = "system_{}.dic".format(DICT_EDITION)


logger = getLogger(__name__)

# Download and place the dictionary file
if not os.path.exists(RESOURCE_DIR):
    logger.warning("Downloading the Sudachi dictionary (It may take a while) ...")
    _, _msg = urlretrieve(ZIP_URL, ZIP_NAME)
    with ZipFile(ZIP_NAME) as z:
        z.extractall()
    os.rename(UNZIP_NAME, RESOURCE_DIR)
    os.rename(os.path.join(RESOURCE_DIR, BINARY_NAME),
              os.path.join(RESOURCE_DIR, "system.dic"))
    os.remove(ZIP_NAME)
    logger.warning("... downloaded and placed the dictionary at `{}`.".format(RESOURCE_DIR))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SudachiDict-{}".format(DICT_EDITION),
    version=PKG_VERSION,
    description="Sudachi Dictionary for SudachiPy - {} Edition".format(DICT_EDITION.title()),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WorksApplications/SudachiDict",
    license="Apache-2.0",
    author="Works Applications",
    author_email="sudachi@worksap.co.jp",
    packages=setuptools.find_packages(),
    package_data={"": ["resources/*"]},
    install_requires=[
        "SudachiPy>=0.5,<0.7"
    ],
)
