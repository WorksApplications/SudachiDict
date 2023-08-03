from pathlib import Path


def validate_file(file: Path) -> Path:
    if file.exists():
        return file
    raise FileNotFoundError(f"required file {file} was not present")
