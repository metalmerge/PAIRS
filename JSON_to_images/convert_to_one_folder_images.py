import json
import os
import requests
from PIL import Image

json_file_path = "JSON_input/ratings_pks70a_unchecked.json"
output_folder_path = "known_JSON_Pulsar_Data"

if not os.path.exists(json_file_path):
    print(f"JSON file not found at {json_file_path}")
else:
    # Load data from the JSON file
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    # Create folder if it does not exist
    os.makedirs(output_folder_path, exist_ok=True)
    # Iterate through the data and download images
    for item in data:
        file_name = item["file"]
        # result = item["checked"]["result"]
        # Download the image
        image_url = item["image_url"]
        response = requests.get(image_url)
        if response.status_code == 200:
            # Save the image to the appropriate folder
            image_path = os.path.join(output_folder_path, file_name)
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
                print(f"Downloaded {file_name} to {output_folder_path}")
            image = Image.open(image_path)
            image.save(image_path)
        else:
            print(f"Failed to download {file_name}")

    print("Download and resize process complete.")
