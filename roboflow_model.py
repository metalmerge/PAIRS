from roboflow import Roboflow
import json

image_path = "/Users/dimaermakov/Downloads/test.png"

rf = Roboflow(api_key="meB2e1C0V6tbgN5Sq88K")
project = rf.workspace().project("pulsar-detection")
model = project.version(1).model

# infer on a local image
json_formatted_str = json.dumps(model.predict(image_path).json(), indent=2)

print(json_formatted_str)

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True).json())

# save an image annotated with your predictions
# model.predict("your_image.jpg").save("prediction.jpg")
