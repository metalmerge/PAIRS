import json
import os
from roboflow import Roboflow


def main():
    base_url = "https://pulsars.nanosta.rs/index.php?viewer&folder="
    json_folder_path = "JSON_input"
    json_output_file_path = "JSON_output/found_Pulsar_Candidates.json"

    if not os.path.exists(json_folder_path):
        print(f"JSON folder not found at {json_folder_path}")
        return

    selected_json_objects = []

    api_key = os.environ.get("ROBOFLOW_API_KEY")
    if api_key is None:
        raise ValueError("ROBOFLOW_API_KEY environment variable is not set.")

    rf = Roboflow(api_key=api_key)
    project = rf.workspace().project("pulsarfinderimageclassification")
    model = project.version(2).model

    print("Model loaded")

    for filename in os.listdir(json_folder_path):
        if filename.endswith(".json"):
            process_json_file(
                os.path.join(json_folder_path, filename),
                base_url,
                model,
                selected_json_objects,
            )

    save_selected_json_objects(json_output_file_path, selected_json_objects)
    print(f"Selected JSON objects saved to {json_output_file_path}")

    num_objects = len(selected_json_objects)
    print("Number of objects in the array:", num_objects)

    os.system(
        'osascript -e \'display notification "Predictions Done" with title "Done"\''
    )
    # os.system("sleep 5")


def process_json_file(json_file_path, base_url, model, selected_json_objects):
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
        for item in data:
            image_filename = item["file"]
            image_path = item["image_url"]
            image_folder = item["folder"]
            link = f"{base_url}{image_folder}&file={image_filename}"
            item["link"] = link
            # if image_folder == "cands_S4.2":
            try:
                predictions = model.predict(image_path, hosted=True).json()
                process_predictions(item, predictions, selected_json_objects)
            except Exception as e:
                print(f"Error: {e} for {image_filename}")


def process_predictions(item, predictions, selected_json_objects):
    top_prediction = predictions["predictions"][0]["top"]
    confidence = predictions["predictions"][0]["confidence"]
    if top_prediction == "pulsar_candidate" and confidence >= 0.99:
        print(f"{item['file']}: {top_prediction} ({confidence})")
        selected_json_objects.append(item)


def save_selected_json_objects(output_path, selected_json_objects):
    with open(output_path, "w") as json_file:
        json.dump(selected_json_objects, json_file, indent=2)


if __name__ == "__main__":
    main()
