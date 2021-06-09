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

In SudachiPy v0.5.2 and later, you can specify a dictionary directly from a command line or program.

**WARNING: `sudachipy link` is no longer available in SudachiPy v0.5.2 and later.**

Please see the following links for more details on the dictionary option.

- english
  - [https://github.com/WorksApplications/SudachiPy#dictionary-edition](https://github.com/WorksApplications/SudachiPy#dictionary-edition)
- japanese
  - [https://github.com/WorksApplications/SudachiPy/blob/develop/docs/tutorial.md#辞書の種類](https://github.com/WorksApplications/SudachiPy/blob/develop/docs/tutorial.md#%E8%BE%9E%E6%9B%B8%E3%81%AE%E7%A8%AE%E9%A1%9E)

### Install

```bash
pip install sudachidict_core
```

```bash
pip install sudachidict_small
```

```bash
pip install sudachidict_full
```

### Dictionary option in SudachiPy before v0.5.2

In case you are using SudachiPy before v0.5.2, please visit the old SudachiPy documentation.

- english
  - [https://github.com/WorksApplications/SudachiPy/tree/v0.5.1#dictionary-edition](https://github.com/WorksApplications/SudachiPy/tree/v0.5.1#dictionary-edition)
- japanese
  - [https://github.com/WorksApplications/SudachiPy/blob/v0.5.1/docs/tutorial.md#%辞書の種類](https://github.com/WorksApplications/SudachiPy/blob/v0.5.1/docs/tutorial.md#%E8%BE%9E%E6%9B%B8%E3%81%AE%E7%A8%AE%E9%A1%9E)
