# Release process

Release process is semi-manual because you need to get new versions of raw Sudachi dictionaries.

## Get access to sudachi artifact storages

1. Sudachi AWS account (with MFA enabled)
2. Token for PyPI publication (long string, starts from `pypi-`)

## Setup release virtual environment

All folders with names starting with `.venv` are ignored in git:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies for build environment

```bash
pip install -r scripts/requirements.txt
```

## Use basic release script

```bash
bash do_release.sh DIC_VERSION /path/to/csv/dics aws-profile arn:aws:iam::0123456789:mfa/iam_user
```

Arguments (positional):
1. Path to csv dictionaries, should contain small_lex.zip, core_lex.zip, notcore_lex.zip files
2. Version for new release (as dictionaries will be uploaded with)
3. Configured profile for AWS for Sudachi
4. MFA arn for the user
5. (optional) version string for Python package

## Setup twine

You need to setup twine login information.
SudachiDict_core is a critial PyPI package and you have to use token-based auth for releases.
Prepare the following login information.
Note that `export` commands here start with spaces and they won't be saved to bash history because of it.

```
 export TWINE_USERNAME=__token__
 export TWINE_PASSWORD=pypi-starting-login-string
 export TWINE_REPOSITORY_URL=https://upload.pypi.org/legacy/
```

## Upload Packages to PyPI

Packages are built into <root>/build/python directory.
We upload all files from `sdist` directory and `wheels` which are less than 100MB.
