import json
import os

import requests
from roboflow import Roboflow

# Define the path to your JSON file
json_file_path = "/Users/dimaermakov/Downloads/pks70_export (1).json"

# Check if the JSON file exists
if not os.path.exists(json_file_path):
    print(f"JSON file not found at {json_file_path}")
else:
    # Load data from the JSON file
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    # Create folders if they don't exist
    folder_path = "Pulsar_Dataset"
    os.makedirs(folder_path, exist_ok=True)

    # Iterate through the data and download images
    for item in data:
        file_name = item["file"]
        result = item["checked"]["result"]

        # Download the image
        image_url = item["remoteUrl"]
        response = requests.get(image_url)

        if response.status_code == 200:
            # Save the image to the appropriate folder
            image_path = os.path.join(folder_path, file_name)
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
                print(f"Downloaded {file_name} to {folder_path}")
        else:
            print(f"Failed to download {file_name}")

    print("Download process complete.")


image_folder_path = "/Users/dimaermakov/PULSAR/Pulsar_Dataset"

# Create the "found_pulsars" folder if it doesn't exist
output_folder = "/Users/dimaermakov/PULSAR/found_pulsars"
os.makedirs(output_folder, exist_ok=True)

# Initialize Roboflow API
rf = Roboflow(api_key="meB2e1C0V6tbgN5Sq88K")
project = rf.workspace().project("pulsar-detection")
model = project.version(1).model


# Function to predict and save images
def predict_and_save(image_path):
    # Predict on the image
    predictions = model.predict(image_path).json()

    # Check if it's "images_without_none" with confidence >= 0.9
    top_prediction = predictions["predictions"][0]["top"]
    confidence = predictions["predictions"][0]["confidence"]

    if top_prediction == "images_without_none" and confidence >= 0.9:
        # Copy the image to the "found_pulsars" folder
        image_name = os.path.basename(image_path)
        output_path = os.path.join(output_folder, image_name)
        os.system(f"cp {image_path} {output_path}")
        print(f"Saved: {image_name}")


# Iterate through images in the folder
for root, _, files in os.walk(image_folder_path):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(root, file)
            predict_and_save(image_path)

print("Prediction and saving process complete.")
