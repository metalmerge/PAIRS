import json
import os
from roboflow import Roboflow

# Define the path to your JSON folder
base_url = "https://pulsars.nanosta.rs/index.php?viewer&folder="
json_folder_path = "JSON"
json_output_file_path = "found_Pulsar_Candidates.json"
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
    project = rf.workspace().project("pulsarfinderimageclassification")
    model = project.version(2).model
    print("Model loaded")
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
                    image_path = item["image_url"]
                    image_folder = item["folder"]
                    link = f"{base_url}{image_folder}&file={image_filename}"
                    item["link"] = link
                    # Predict on the local image
                    # if image_folder == "cands_S4.2":
                    try:
                        predictions = model.predict(image_path, hosted=True).json()
                        top_prediction = predictions["predictions"][0]["top"]
                        confidence = predictions["predictions"][0]["confidence"]
                        if top_prediction == "pulsar_candidate" and confidence >= 0.99:
                            print(f"{image_filename}: {top_prediction} ({confidence})")
                            selected_json_objects.append(item)
                    except Exception as e:
                        print(f"Error: {image_filename}")
    # Save the selected JSON objects as a JSON file
    with open(json_output_file_path, "w") as json_file:
        json.dump(selected_json_objects, json_file, indent=2)
    print(f"Selected JSON objects saved to {json_output_file_path}")
    with open(json_output_file_path, "r") as file:
        data = json.load(file)
    # Count the number of objects in the array
    num_objects = len(data)
    # Print the number of objects
    print("Number of objects in the array:", num_objects)
    os.system(
        'osascript -e \'display notification "Predictions Done" with title "Done"\''
    )
    os.system("sleep 5")
