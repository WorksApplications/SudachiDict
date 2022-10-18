# SudachiDict

A lexicon for Japanese tokenizer
[Sudachi](https://github.com/WorksApplications/Sudachi/).

## Download

Click [here](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/) for pre-built dictionaries.

Pre-built synonym dictionaries for [Chikkar](https://github.com/WorksApplications/chikkar/) is [here](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachisynonym/).

### Python packages

You can install the dictionaries for [WorksApplications/SudachiPy](https://github.com/WorksApplications/SudachiPy), the Python version of Sudachi, as Python packages.

In SudachiPy v0.5.2 and later, you can specify a dictionary directly from a command line or program.

**WARNING: `sudachipy link` is no longer available in SudachiPy v0.5.2 and later.**

please see the following links for more details on the dictionary option.

- english
  - [https://github.com/WorksApplications/SudachiPy#dictionary-edition](https://github.com/WorksApplications/SudachiPy#dictionary-edition)
- japanese
  - [https://github.com/WorksApplications/SudachiPy/blob/develop/docs/tutorial.md#辞書の種類](https://github.com/WorksApplications/SudachiPy/blob/develop/docs/tutorial.md#%E8%BE%9E%E6%9B%B8%E3%81%AE%E7%A8%AE%E9%A1%9E)

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

## Dictionary types

Sudachi has three types of dictionaries.

- Small: includes only the vocabulary of UniDic
- Core: includes basic vocabulary (default)
- Full: includes miscellaneous proper nouns

## Build from sources


Dictionary sources were hosted on git lfs, but [are hosted on S3](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict-raw/) now.
They will be moved to github in the future once more.

At the moment, you need to manually download required files from the AWS S3, and unzip them into the `src/main/text` directory.
Core dictionary requires small and core files, Full requires all three files.

## Licenses

```text
SudachiDict by Works Applications Co., Ltd. is licensed under the [Apache License, Version2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

   Copyright (c) 2017 Works Applications Co., Ltd.

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

- <http://unidic.ninjal.ac.jp/>
- <https://github.com/neologd/mecab-ipadic-neologd>
