# this file has to be run for testing img inspector

from image_inspector.inspector import ImageInspector

insp = ImageInspector("./testset/images")

# Store and print the results returned by inspect()
results = insp.inspect()
print(results)