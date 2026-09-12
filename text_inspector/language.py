from langdetect import detect
from langdetect import LangDetectException


class LanguageCheck:

    @staticmethod
    def check(df):
        supported = df[
            df["supported"]
        ].copy()

        languages = []

        print("\nLanguage Detection")
        print("-" * 20)

        for _, row in supported.iterrows():
            file = row["file"]

            try:
                with open(
                    file,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:
                    text = f.read()

                if not text.strip():
                    language = "Empty"

                elif len(text.strip()) < 20:
                    language = "Too Short"

                else:
                    language = detect(text)

                print(
                    f"{file.name}: "
                    f"{language}"
                )

            except LangDetectException:
                language = "Unknown"

                print(
                    f"{file.name}: Unknown"
                )

            except Exception as e:
                language = "Error"

                print(
                    f"{file.name}: Error ({e})"
                )

            languages.append(language)

        supported["language"] = languages

        return supported