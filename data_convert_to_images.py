"""
Downloads and resizes images from a JSON file containing image URLs and metadata.

This script reads a JSON file containing image URLs and associated metadata, downloads the images, and resizes them to a specific dimensions (1100x850 pixels). The downloaded images are saved to a folder named "Pulsar_Dataset" in the current working directory.

Make sure to specify the path to the JSON file in the 'json_file_path' variable.

Requirements:
- Install the 'requests' library: pip install requests
- Install the 'Pillow' library (PIL): pip install Pillow
- Install the 'roboflow' library if not already installed.

Usage:
1. Set the 'json_file_path' variable to the path of the JSON file containing image URLs.
2. Run the script to download and resize the images.

Note: Ensure that the required libraries are installed and that you have an active internet connection to download the images.

Author: Dimitry Ermakov
"""
import json
import os
import requests
from PIL import Image
from roboflow import Roboflow

json_file_path = "ratings_pks70a_unchecked.json"

if not os.path.exists(json_file_path):
    print(f"JSON file not found at {json_file_path}")
else:
    # Load data from the JSON file
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    # Create folders if they don't exist
    output_folder_path_of_images = "pulsar_Images_Dataset"
    os.makedirs(output_folder_path_of_images, exist_ok=True)

    # Iterate through the data and download images
    for item in data:
        file_name = item["file"]
        # result = item["checked"]["result"]

        # Download the image
        image_url = item["image_url"]
        response = requests.get(image_url)

        if response.status_code == 200:
            # Save the image to the appropriate folder
            image_path = os.path.join(output_folder_path_of_images, file_name)
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
                print(f"Downloaded {file_name} to {output_folder_path_of_images}")
            image = Image.open(image_path)
            image = image.resize((1100, 850))
            image.save(image_path)
        else:
            print(f"Failed to download {file_name}")

    print("Download and resize process complete.")
