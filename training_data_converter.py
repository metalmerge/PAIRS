import os
import requests
import json

# Define the path to your JSON file
json_file_path = "path_to_your_json_file.json"

# Check if the JSON file exists
if not os.path.exists(json_file_path):
    print(f"JSON file not found at {json_file_path}")
else:
    # Load data from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Create folders if they don't exist
    folder_none = "images_with_none"
    folder_other = "images_without_none"
    os.makedirs(folder_none, exist_ok=True)
    os.makedirs(folder_other, exist_ok=True)

    # Iterate through the data and download images
    for item in data:
        file_name = item["file"]
        result = item["checked"]["result"]

        # Determine the folder based on the result
        if result == "&lt;none&gt;":
            folder_path = folder_none
        else:
            folder_path = folder_other

        # Download the image
        image_url = item["remoteUrl"]
        response = requests.get(image_url)

        if response.status_code == 200:
            # Save the image to the appropriate folder
            image_path = os.path.join(folder_path, file_name)
            with open(image_path, 'wb') as image_file:
                image_file.write(response.content)
                print(f"Downloaded {file_name} to {folder_path}")
        else:
            print(f"Failed to download {file_name}")

    print("Download process complete.")
