import os
import requests
import json

# Define the path to the folder containing JSON files
json_folder_path = "/Users/dimaermakov/Downloads/Known_Pulsar_Data_JSON"

# Check if the folder exists
if not os.path.exists(json_folder_path):
    print(f"JSON folder not found at {json_folder_path}")
else:
    # Define the target folder for downloading images
    target_folder = "/Users/dimaermakov/Downloads/4.3"
    os.makedirs(target_folder, exist_ok=True)

    # Iterate through the JSON files in the folder
    for filename in os.listdir(json_folder_path):
        if filename.endswith(".json"):
            json_file_path = os.path.join(json_folder_path, filename)

            # Load data from the JSON file
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

            # Iterate through the data and download images from "cands_S4.3" folder
            for item in data:
                folder = item.get("folder", "")

                # Check if the folder matches "cands_S4.3"
                if folder == "cands_S4.3":
                    file_name = item["file"]
                    image_url = item["image_url"]

                    # Download the image
                    response = requests.get(image_url)

                    if response.status_code == 200:
                        # Save the image to the "4.3" folder
                        image_path = os.path.join(target_folder, file_name)
                        with open(image_path, "wb") as image_file:
                            image_file.write(response.content)
                            print(f"Downloaded {file_name} to {target_folder}")
                    else:
                        print(f"Failed to download {file_name}")

    print("Download process complete.")
