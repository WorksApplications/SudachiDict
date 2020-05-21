# Sudachi Dictionary for SudachiPy

- [WorksApplications/SudachiDict](https://github.com/WorksApplications/SudachiDict)
- [WorksApplications/SudachiPy](https://github.com/WorksApplications/SudachiPy)

Managing the dictionary resources as Python packages.

- [SudachiDict-small · PyPI](https://pypi.org/project/SudachiDict-small/)
- [SudachiDict-core · PyPI](https://pypi.org/project/SudachiDict-core/)
- [SudachiDict-full · PyPI](https://pypi.org/project/SudachiDict-full/)

The dictionary files are not included in the packages; It will be downloaded upon installation (the procedure in `setup.py`).

The version (e.g., `20200330`) and the edition (`small`, `core`, or `full`) is specified in `INFO.json`.


## Commands to download and set the dictionaries

```bash
$ pip install sudachidict_core
```

```bash
$ pip install sudachidict_small
$ sudachipy link -t small
```

```bash
$ pip install sudachidict_full
$ sudachipy link -t full
```
