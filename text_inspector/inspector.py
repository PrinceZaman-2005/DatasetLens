from pathlib import Path

from .metadata import Metadata
from .format_check import FormatCheck


class TextInspector:

    def __init__(self, address: str):
        self.address = Path(address)

        if not self.address.exists():
            raise FileNotFoundError(
                f"Path does not exist: {self.address}"
            )

        self.path_type = Metadata.get_path_type(
            self.address
        )

        self.files = Metadata.get_files(
            self.address
        )

        self.df = Metadata.build(
            self.files,
            FormatCheck.SUPPORTED_FORMATS
        )

    def files_count(self):
        total = len(self.df)

        print(f"\nTotal files: {total}")

        return total

    def check_formats(self):
        return FormatCheck.check(
            self.df
        )

    def supported_files(self):
        return FormatCheck.supported(
            self.df
        )

    def unsupported_files(self):
        return FormatCheck.unsupported(
            self.df
        )

    def inspect(self):
        print("\nDatasetLens - Text Inspector")
        print("=" * 30)

        self.files_count()
        self.check_formats()
        self.supported_files()
        self.unsupported_files()

        return self.df

    def __repr__(self):
        return (
            f"TextInspector("
            f"address='{self.address}', "
            f"type='{self.path_type}', "
            f"files={len(self.df)})"
        )