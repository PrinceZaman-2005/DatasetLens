from charset_normalizer import from_bytes


class EncodingCheck:

    @staticmethod
    def check(df):
        supported = df[
            df["supported"]
        ].copy()

        encodings = []

        print("\nEncoding Detection")
        print("-" * 20)

        for _, row in supported.iterrows():
            file = row["file"]

            try:
                with open(file, "rb") as f:
                    raw = f.read()

                result = from_bytes(raw).best()

                if result is not None:
                    encoding = result.encoding
                else:
                    encoding = "Unknown"

                print(
                    f"{file.name}: "
                    f"{encoding}"
                )

            except Exception as e:
                encoding = "Error"

                print(
                    f"{file.name}: Error ({e})"
                )

            encodings.append(encoding)

        supported["encoding"] = encodings

        return supported