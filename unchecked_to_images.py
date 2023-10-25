import json
import os
import requests
from PIL import Image
from roboflow import Roboflow

# Define the path to your JSON file
json_file_path = "ratings_Unchecked.json"
image_folder_path = "/Pulsar_Dataset_unchecked"
output_folder_path = "found_Pulsars_Images_Dataset"
os.makedirs(output_folder_path, exist_ok=True)

# Initialize Roboflow API
api_key = os.environ.get("ROBOFLOW_API_KEY")

if api_key is None:
    raise ValueError("ROBOFLOW_API_KEY environment variable is not set.")

rf = Roboflow(api_key=api_key)
project = rf.workspace().project("updated-pulsar-database")
model = project.version(1).model

saved_file_count = 0


# Function to predict and save images
def predict_and_save(image_path):
    global saved_file_count
    # Predict on the image
    predictions = model.predict(image_path).json()

    # Check if it's "images_without_none" with confidence >= 0.9
    top_prediction = predictions["predictions"][0]["top"]
    confidence = predictions["predictions"][0]["confidence"]

    if top_prediction == "pulsar_candidate" and confidence >= 0.994:
        image_name = os.path.basename(image_path)

        if not os.path.exists(os.path.join(output_folder_path, image_name)):
            # Copy the image to the "found_pulsars" folder
            print(f"Found pulsar: {confidence}")
            output_path = os.path.join(output_folder_path, image_name)
            os.system(f"cp {image_path} {output_path}")
            print(f"Saved: {image_name}")
            saved_file_count += 1
        else:
            print(f"File with the same name already exists: {image_name}")
        # if saved_file_count >= 100:
        #     print("Reached the limit of 100 saved files. Stopping.")
        #     # Exit the function to stop processing more files
        #     os.system(
        #         'osascript -e \'display notification "Predictions Done" with title "Done"\''
        #     )
        #     exit()


# Iterate through images in the folder
for root, _, files in os.walk(image_folder_path):
    for file in files:
        image_path = os.path.join(root, file)
        predict_and_save(image_path)

print("Prediction and saving process complete.")
os.system('osascript -e \'display notification "Predictions Done" with title "Done"\'')
