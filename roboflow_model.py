import json
import os
import requests
from PIL import Image
from roboflow import Roboflow

# Define the path to your JSON file
json_file_path = "/Users/dimaermakov/Downloads/ratings_pks70a_unchecked.json"

# Check if the JSON file exists
# if not os.path.exists(json_file_path):
#     print(f"JSON file not found at {json_file_path}")
# else:
#     # Load data from the JSON file
#     with open(json_file_path, "r") as json_file:
#         data = json.load(json_file)

#     # Create folders if they don't exist
#     folder_path = "Pulsar_Dataset"
#     os.makedirs(folder_path, exist_ok=True)

#     # Iterate through the data and download images
#     for item in data:
#         file_name = item["file"]
#         # result = item["checked"]["result"]

#         # Download the image
#         image_url = item["image_url"]
#         response = requests.get(image_url)

#         if response.status_code == 200:
#             # Save the image to the appropriate folder
#             image_path = os.path.join(folder_path, file_name)
#             with open(image_path, "wb") as image_file:
#                 image_file.write(response.content)
#                 print(f"Downloaded {file_name} to {folder_path}")
#             image = Image.open(image_path)
#             image = image.resize((1100, 850))
#             image.save(image_path)
#         else:
#             print(f"Failed to download {file_name}")

#     print("Download and resize process complete.")

image_folder_path = "/Users/dimaermakov/Downloads/Pulsar_Dataset_unchecked"

# Create the "found_pulsars" folder if it doesn't exist
output_folder = "/Users/dimaermakov/PULSAR/found_pulsars"
os.makedirs(output_folder, exist_ok=True)

# Initialize Roboflow API
rf = Roboflow(api_key="meB2e1C0V6tbgN5Sq88K")
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

    if top_prediction == "pulsars" and confidence >= 0.994:
        image_name = os.path.basename(image_path)

        if not os.path.exists(os.path.join(output_folder, image_name)):
            # Copy the image to the "found_pulsars" folder
            print(f"Found pulsar: {confidence}")
            output_path = os.path.join(output_folder, image_name)
            os.system(f"cp {image_path} {output_path}")
            print(f"Saved: {image_name}")
            saved_file_count += 1
        else:
            print(f"File with the same name already exists: {image_name}")
        if saved_file_count >= 150:
            print("Reached the limit of 150 saved files. Stopping.")
            # Exit the function to stop processing more files
            os.system(
                'osascript -e \'display notification "Predictions Done" with title "Done"\''
            )
            exit()


# Iterate through images in the folder
for root, _, files in os.walk(image_folder_path):
    for file in files:
        image_path = os.path.join(root, file)
        predict_and_save(image_path)

print("Prediction and saving process complete.")
os.system('osascript -e \'display notification "Predictions Done" with title "Done"\'')
