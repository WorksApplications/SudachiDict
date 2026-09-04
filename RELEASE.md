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
bash do_release.sh FORMAT_VERSION DIC_VERSION /path/to/zipped/csv/dics aws-profile arn:aws:iam::0123456789:mfa/iam_user

# ex.
# ./lexicons/v0/
#   - small_lex.zip
#   - core_lex.zip
#   - notcore_lex.zip
bash do_release.sh v0 20260901 ./lexicons/v0 aws-profile arn:aws:iam::0123456789:mfa/iam_user
```

Arguments (positional):
1. Format version to work with (`v0` or `v1`)
2. Version for new release (as dictionaries will be uploaded with), `YYYYMMDD`
3. Path to zipped csv dictionaries, should contain small_lex.zip, core_lex.zip, notcore_lex.zip files
  - Note that although v0/v1 uses the same file names, their content is different (lexicon csv also has v0/v1 format).
4. Configured profile for AWS for Sudachi
5. MFA arn for the user
6. (optional) version string for Python package

This kicks python packaging only when the format version is `v0`.

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
