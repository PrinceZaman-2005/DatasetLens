# inspectors/text_insp.py

from pathlib import Path
import pandas as pd


class TextInspector:

    SUPPORTED_FORMATS = {
        ".txt",
        ".csv",
        ".json",
        ".jsonl",
        ".xml",
        ".md",
        ".tsv",
        ".yaml",
        ".yml"
    }

    def __init__(self, address: str):
        self.address = Path(address)

        if not self.address.exists():
            raise FileNotFoundError(
                f"Path does not exist: {self.address}"
            )

        self.path_type = (
            "file"
            if self.address.is_file()
            else "directory"
        )

        if self.path_type == "file":
            self.files = [self.address]

        else:
            self.files = [
                file
                for file in self.address.rglob("*")
                if file.is_file()
            ]

        # Dataset metadata
        self.df = pd.DataFrame({
            "file": self.files,
            "name": [file.name for file in self.files],
            "format": [
                file.suffix.lower()
                for file in self.files
            ],
            "size_bytes": [
                file.stat().st_size
                for file in self.files
            ]
        })

        self.df["supported"] = (
            self.df["format"]
            .isin(self.SUPPORTED_FORMATS)
        )

    def files_count(self):
        total = len(self.df)

        print(f"\nTotal files: {total}")

        return total

    def check_formats(self):
        formats = (
            self.df["format"]
            .value_counts()
            .to_dict()
        )

        print("\nFormat Distribution")
        print("-" * 20)

        for ext, count in formats.items():
            print(f"{ext}: {count}")

        return formats

    def supported_files(self):
        supported = self.df[
            self.df["supported"]
        ]

        print(
            f"Supported files: {len(supported)}"
        )

        return supported

    def unsupported_files(self):
        unsupported = self.df[
            ~self.df["supported"]
        ]

        print(
            f"Unsupported files: {len(unsupported)}"
        )

        if not unsupported.empty:
            print("\nUnsupported Formats Found")

            for _, row in unsupported.iterrows():
                print(
                    f"- {row['name']}"
                )

        return unsupported

    def detect_encoding(self):
        supported = self.supported_files()

        print(
            f"\nScanning {len(supported)} files..."
        )

        for file in supported["file"]:
            print(
                f"Detecting encoding: {file.name}"
            )

        return supported

    def __repr__(self):
        return (
            f"TextInspector("
            f"address='{self.address}', "
            f"type='{self.path_type}', "
            f"files={len(self.df)})"
        )