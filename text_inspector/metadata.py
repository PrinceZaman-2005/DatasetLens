from pathlib import Path

import pandas as pd


class Metadata:

    @staticmethod
    def get_path_type(address):
        address = Path(address)

        return (
            "file"
            if address.is_file()
            else "directory"
        )

    @staticmethod
    def get_files(address):
        address = Path(address)

        if Metadata.get_path_type(address) == "file":
            return [address]

        return [
            file
            for file in address.rglob("*")
            if file.is_file()
        ]

    @staticmethod
    def build(files, supported_formats):
        df = pd.DataFrame({
            "file": files,
            "name": [
                file.name
                for file in files
            ],
            "format": [
                file.suffix.lower()
                for file in files
            ],
            "size_bytes": [
                file.stat().st_size
                for file in files
            ]
        })

        df["supported"] = (
            df["format"]
            .isin(supported_formats)
        )

        return df