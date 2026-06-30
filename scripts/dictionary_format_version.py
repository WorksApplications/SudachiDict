from enum import Enum

class DictionaryFormatVersion(Enum):
    V0 = "v0"
    V1 = "v1"

    def s3_prefix(self) -> str:
        if self is DictionaryFormatVersion.V0:
            # put V0 files under root to keep backward compatibiity
            return ""
        if self is DictionaryFormatVersion.V1:
            return "/v1"
        
        raise ValueError("Unknown format version")


def main():
    print(DictionaryFormatVersion("v0"))
    print(DictionaryFormatVersion("v1"))


if __name__ == '__main__':
    main()
