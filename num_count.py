import json

JSON_url = "ratings_unchecked.json"
# Read the JSON data from the file
with open(JSON_url, "r") as file:
    data = json.load(file)
# Count the number of objects in the array
num_objects = len(data)
# Print the number of objects
print("Number of objects in the array:", num_objects)
