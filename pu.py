import json

# Load the JSON data from the file
with open('WLASL_v0.3.json', 'r') as file:
    data = json.load(file)

# Extract all 'gloss' values
gloss_values = [item["gloss"] for item in data]

# Output the gloss values
print(gloss_values)
