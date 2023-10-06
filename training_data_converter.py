import os
import requests
import json

# Define the path to the folder containing JSON files
json_folder_path = "/Users/dimaermakov/Downloads/Known_Pulsar_Data_JSON"

# Check if the folder exists
if not os.path.exists(json_folder_path):
    print(f"JSON folder not found at {json_folder_path}")
else:
    # Iterate through the JSON files in the folder
    for filename in os.listdir(json_folder_path):
        if filename.endswith(".json"):
            json_file_path = os.path.join(json_folder_path, filename)

            # Load data from the JSON file
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

            # Create folders if they don't exist
            folder_path = "/Users/dimaermakov/Downloads/Pulsar_Dataset_unchecked"
            os.makedirs(folder_path, exist_ok=True)

            # Iterate through the data and download images
            for item in data:
                file_name = item["file"]
                # result = item["checked"]["result"]

                # Determine the folder based on the result

                # Download the image
                image_url = item["image_url"]
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
os.system("sleep 5")
