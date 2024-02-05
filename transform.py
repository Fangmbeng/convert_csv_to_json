import csv
import json

csv_file_path = 'georefusa.csv'  # Path to your CSV file
json_file_path = 'georefusa.json'  # Path to save JSON file

data = []

state_abbreviations = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming",
    "AS": "American Samoa", "DC": "District of Columbia", "GU": "Guam",
    "MP": "Northern Mariana Islands", "PR": "Puerto Rico", "VI": "Virgin Islands"
}

# Populate the data variable with all US states
data1 = [{"State": state} for state in state_abbreviations.keys()]
pk={}

# Convert CSV data to JSON format
converted_json = []
for index, entry in enumerate(data1, start=1):
    # Check if the state name exists in the mapping
    state_name = entry['State']
    pk[state_name]=index
    if state_name in state_abbreviations:
        state_abbreviation = state_abbreviations[state_name]
    else:
        # Use the original name if no abbreviation is found
        state_abbreviation = state_name

    new_entry = {
        "model": "geo.state",
        "pk": index,  # Modify pk to integers ranging from 1 to the number of entries
        "fields": {
            "name": state_abbreviation,
            "abbreviation": state_name,
            "country": "1",  # Assuming all entries belong to the US
        }
    }
    converted_json.append(new_entry)

# Replace values in the sample JSON with the converted CSV data
json_data = converted_json

# Save the updated JSON
with open('converted_state.json', 'w') as f:
    json.dump(json_data, f, indent=4)

print(pk)

# Read data from CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

pk1={}
# Convert CSV data to JSON format
converted_json1 = []
for index, entry in enumerate(data, start=1):
    pk1[entry['City']]=index
    new_entry = {
        "model": "geo.city",
        "pk": index,  # Modify pk to integers ranging from 1 to the number of entries
        "fields": {
            "name": entry['City'],
            "state": pk[entry['State']]
        }
    }
    converted_json1.append(new_entry)

# Replace values in the sample JSON with the converted CSV data
json_data = converted_json1

# Save the updated JSON
with open('converted_sample.json', 'w') as f:
    json.dump(json_data, f, indent=4)


# Convert CSV data to JSON format
converted_json2 = []
for index, entry in enumerate(data, start=1):
    new_entry = {
        "model": "geo.zip",
        "pk":  index,  # Modify pk to integers ranging from 1 to the number of entries
        "fields": {
            "code": entry['Zip Code'],
            "city": pk1[entry['City']]
        }
    }
    converted_json2.append(new_entry)

# Replace values in the sample JSON with the converted CSV data
json_data = converted_json2

# Save the updated JSON
with open('converted_zip_code.json', 'w') as f:
    json.dump(json_data, f, indent=4)
