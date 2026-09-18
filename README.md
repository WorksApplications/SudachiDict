# SudachiDict

A lexicon for Japanese tokenizer [Sudachi](https://github.com/WorksApplications/Sudachi/) and [sudachi.rs/SudachiPy](https://github.com/WorksApplications/sudachi.rs).

## Dictionary types

Sudachi has three types of dictionaries.

- Small: includes only the vocabulary of UniDic
- Core: includes basic vocabulary (default)
- Full: includes miscellaneous proper nouns

### Dictionary format version

> **IMPORTANT**
> Dictionary binary format is changed to V1 from v202610.

There are two distinct versions:

- V1
  - Supported by Sudachi v0.8.2, sudachi.rs/SudachiPy v0.7, and latter.
- V0
  - Supported by Sudachi v0.8.1, sudachi.rs/SudachiPy v0.6, and former.

Those formats are not compatible each other. You must use the corresponding version with the Sudachi/sudachi.rs/SudachiPy.
Note that from v202610 the assets in the github release pages are V1 format. If you want to use V0 binary of newer source versions, you must get the V0 source files and build it by yourself.

## Download

Click [here](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/v1) for pre-built V1 dictionaries.
You can get source csv files from [here](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict-raw/v1).

If you want V0 format dictionary, access followings.
We will stop releasing V0 dictionary in the future.
- [Binary dictionary (V0)](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/v0)
- [Source file (V0)](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict-raw/v0)

Pre-built synonym dictionaries for [Chikkar](https://github.com/WorksApplications/chikkar/) is [here](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachisynonym/).

### Python packages

You can install the dictionaries for [WorksApplications/SudachiPy](https://github.com/WorksApplications/sudachi.rs/tree/develop/python), the Python version of Sudachi, as Python packages.

> **IMPORTANT**
> From v202610, SudachiDict-* provides the dictionary in new binary format (V1).
> As the V0/V1 binaries are incompatible, SudachiPy v0.7 requires that or latter SudachiDict versions, and SudachiPy v0.6 requires former versions.

In SudachiPy v0.5.2 and later, you can specify a dictionary directly from a command line or program.

> **WARNING: `sudachipy link` is no longer available in SudachiPy v0.5.2 and later.**

please see the following links for more details on the dictionary option.

- english
  - [https://github.com/WorksApplications/sudachi.rs/tree/develop/python#dictionary-edition](https://github.com/WorksApplications/sudachi.rs/tree/develop/python#dictionary-edition)

#### Install

```bash
pip install sudachidict_core
```

```bash
pip install sudachidict_small
```

```bash
pip install sudachidict_full
```

- [SudachiDict-small · PyPI](https://pypi.org/project/SudachiDict-small/)
- [SudachiDict-core · PyPI](https://pypi.org/project/SudachiDict-core/)
- [SudachiDict-full · PyPI](https://pypi.org/project/SudachiDict-full/)

## Build from sources

Dictionary sources were hosted on git lfs, but [are hosted on S3](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict-raw/v1) now.
They will be moved to github in the future once more.

At the moment, you need to manually download required files from the AWS S3, and unzip them into the `src/main/text` directory.
Core dictionary requires small and core files, Full requires all three files.

V0 format source files are disributed [here](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict-raw/v0) (we will stop releasing V0 dictionary in the future).

## Licenses

```text
SudachiDict by Works Applications Co., Ltd. is licensed under the [Apache License, Version2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

   Copyright (c) 2017-2023 Works Applications Co., Ltd.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

This project includes UniDic and a part of NEologd.
```

- <https://clrd.ninjal.ac.jp/unidic/>
- <https://github.com/neologd/mecab-ipadic-neologd>
