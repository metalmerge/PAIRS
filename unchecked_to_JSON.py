import json
import os
from roboflow import Roboflow

# Define the path to your JSON folder
json_folder_path = "/Users/dimaermakov/Downloads/Known_Pulsar_Data_JSON"

# Check if the folder exists
if not os.path.exists(json_folder_path):
    print(f"JSON folder not found at {json_folder_path}")
else:
    # Create a list to store the selected JSON objects
    selected_json_objects = []

    # Initialize Roboflow API
    api_key = os.environ.get("ROBOFLOW_API_KEY")

    if api_key is None:
        raise ValueError("ROBOFLOW_API_KEY environment variable is not set.")

    rf = Roboflow(api_key=api_key)
    project = rf.workspace().project("updated-pulsar-database")
    model = project.version(1).model

    # Define the path to your image folder
    image_folder_path = "/Users/dimaermakov/Downloads/Pulsar_Dataset_unchecked"

    # Iterate through the JSON files in the folder
    for filename in os.listdir(json_folder_path):
        if filename.endswith(".json"):
            json_file_path = os.path.join(json_folder_path, filename)

            # Load data from the JSON file
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

                # Iterate through the data and check confidence
                for item in data:
                    image_filename = item["file"]
                    image_path = os.path.join(image_folder_path, image_filename)

                    # Predict on the local image
                    predictions = model.predict(image_path).json()
                    top_prediction = predictions["predictions"][0]["top"]
                    confidence = predictions["predictions"][0]["confidence"]

                    if top_prediction == "pulsars" and confidence >= 0.994:
                        selected_json_objects.append(item)
                        print(item)

                        # If we've reached 100 selected items, stop
                        if len(selected_json_objects) >= 100:
                            break

                # If we've reached 100 selected items, stop processing more files
                if len(selected_json_objects) >= 100:
                    break

    # Define the path to save the selected JSON objects as a JSON file
    json_output_file = (
        "/Users/dimaermakov/Downloads/selected_json_objects_that_are_unchecked.json"
    )

    # Save the selected JSON objects as a JSON file
    with open(json_output_file, "w") as json_file:
        json.dump(selected_json_objects, json_file, indent=2)

    print(f"Selected JSON objects saved to {json_output_file}")
