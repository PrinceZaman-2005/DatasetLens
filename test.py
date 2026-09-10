from inspectors.text_insp import TextInspector

insp = TextInspector("./testset")

print(insp)

insp.files_count()
insp.check_formats()
insp.supported_files()
insp.unsupported_files()
insp.detect_encoding()