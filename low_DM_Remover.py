import json
import requests
import PIL.Image
import pytesseract
from io import BytesIO


# Function to extract text from coordinates
def extract_text_from_coordinates(image_url, x1, y1, x2, y2):
    response = requests.get(image_url)
    if response.status_code == 200:
        image = PIL.Image.open(BytesIO(response.content))
        region = image.crop((x1, y1, x2, y2))
        text = pytesseract.image_to_string(region)
        return text.strip()
    return None


# Load the JSON file
with open("JSON_output/found_Pulsar_Candidates.json", "r") as json_file:
    data = json.load(json_file)

# Filter and create a new JSON file
filtered_data = []

for item in data:
    image_url = item.get("image_url")
    print(image_url)
    if image_url:
        text = extract_text_from_coordinates(image_url, 826, 138, 933, 156)
        print(text)
        if len(text) > 1:
            filtered_data.append(item)

# Save the filtered data to a new JSON file
with open("output.json", "w") as output_file:
    json.dump(filtered_data, output_file, indent=4)

print("Extraction and filtering complete. Check 'output.json' for the filtered data.")
