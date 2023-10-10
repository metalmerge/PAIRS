import json
import os
import requests
from PIL import Image
from roboflow import Roboflow

json_file_path = "/Users/dimaermakov/Downloads/ratings_pks70a_unchecked.json"

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
        # result = item["checked"]["result"]

        # Download the image
        image_url = item["image_url"]
        response = requests.get(image_url)

        if response.status_code == 200:
            # Save the image to the appropriate folder
            image_path = os.path.join(folder_path, file_name)
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
                print(f"Downloaded {file_name} to {folder_path}")
            image = Image.open(image_path)
            image = image.resize((1100, 850))
            image.save(image_path)
        else:
            print(f"Failed to download {file_name}")

    print("Download and resize process complete.")
