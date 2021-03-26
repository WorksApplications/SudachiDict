# SudachiDict

A lexicon for Japanese tokenizer
[Sudachi](https://github.com/WorksApplications/Sudachi/).

## Download

Click [here](http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/) for pre-built dictionaries.

### Python packages

You can install the dictionaries for [WorksApplications/SudachiPy](https://github.com/WorksApplications/SudachiPy), the Python version of Sudachi, as Python packages.

In SudachiPy v0.5.2 and later, you can specify a dictionary directly from a command line or program.

**WARNING: `sudachipy link` is no longer available in SudachiPy v0.5.2 and later.**

please see the following links for more details on the dictionary option.

* english
    * [https://github.com/WorksApplications/SudachiPy#dictionary-edition](https://github.com/WorksApplications/SudachiPy#dictionary-edition)
* japanese
    * [https://github.com/WorksApplications/SudachiPy/blob/develop/docs/tutorial.md#辞書の種類](https://github.com/WorksApplications/SudachiPy/blob/develop/docs/tutorial.md#%E8%BE%9E%E6%9B%B8%E3%81%AE%E7%A8%AE%E9%A1%9E)

#### Install

```bash
$ pip install sudachidict_core
```

```bash
$ pip install sudachidict_small
```

```bash
$ pip install sudachidict_full
```

* [SudachiDict-small · PyPI](https://pypi.org/project/SudachiDict-small/)
* [SudachiDict-core · PyPI](https://pypi.org/project/SudachiDict-core/)
* [SudachiDict-full · PyPI](https://pypi.org/project/SudachiDict-full/)


## Dictionary types

Sudachi has three types of dictionaries.

* Small: includes only the vocabulary of UniDic
* Core: includes basic vocabulary (default)
* Full: includes miscellaneous proper nouns

## Build from sources

SudachiDict needs [Git LFS](https://git-lfs.github.com/) to download the sourses
of the system dictionaries. If you fail to build the dictionaries, install
Git LFS and `git lfs pull`.

Building the dictionaries fails with a locale other than UTF-8.
Add `-Dfile.encoding=UTF-8` to `MAVEN_OPTS`.


## Licenses

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

- http://unidic.ninjal.ac.jp/
- https://github.com/neologd/mecab-ipadic-neologd
