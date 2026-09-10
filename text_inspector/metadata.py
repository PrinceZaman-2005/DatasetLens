from pathlib import Path

import pandas as pd


class Metadata:

    @staticmethod
    def build(files, supported_formats):
        df = pd.DataFrame({
            "file": files,
            "name": [file.name for file in files],
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