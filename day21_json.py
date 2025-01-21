# Day 21: working with JSON for my practice

import json

# My basic JSON (1)
my_person_dict = {
    "name": "David",
    "age": 30,
    "city": "Asheville",
    "hobbies": ["hiking", "coding"]
}

# My JSON string
my_json_string = json.dumps(my_person_dict)
print("My JSON:", my_json_string)

# My pretty JSON (2)
my_pretty_json = json.dumps(my_person_dict, indent=2)
print("My pretty JSON:")
print(my_pretty_json)

# My parsing JSON (3)
my_json_text = '{"name": "Taylor", "age": 28, "city": "Durham"}'
my_parsed = json.loads(my_json_text)
print("My parsed name:", my_parsed["name"])
print("My parsed age:", my_parsed["age"])

# My JSON with nested objects (4)
my_team = {
    "team_name": "My Team",
    "members": [
        {"name": "David", "role": "lead"},
        {"name": "Taylor", "role": "dev"},
        {"name": "Alex", "role": "tester"}
    ]
}

my_team_json = json.dumps(my_team, indent=2)
print("My team JSON:")
print(my_team_json)

# My parsing nested JSON (5)
my_team_str = '{"team":"Python","members":["David","Taylor","Alex"]}'
my_team_data = json.loads(my_team_str)
print("My team:", my_team_data["team"])
print("My first member:", my_team_data["members"][0])

# My JSON file writing (6)
my_file_data = {
    "name": "Scout",
    "breed": "mixed",
    "age": 3,
    "favorite_activities": ["running", "playing", "napping"]
}

with open("my_dog_data.json", "w") as my_f:
    json.dump(my_file_data, my_f, indent=2)
print("I wrote JSON to file")

# My JSON file reading (7)
with open("my_dog_data.json", "r") as my_f:
    my_loaded_data = json.load(my_f)
print("My loaded dog:", my_loaded_data["name"])
print("My dog's age:", my_loaded_data["age"])

# My JSON with default handling (8)
from datetime import datetime

my_data_with_date = {
    "name": "David",
    "created": datetime.now()
}

# This will fail without special handling
try:
    my_json = json.dumps(my_data_with_date)
except TypeError as e:
    print(f"My error: {e}")

# My JSON with custom encoder (9)
class MyDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

my_json_with_date = json.dumps(my_data_with_date, cls=MyDateTimeEncoder)
print("My JSON with date:", my_json_with_date)

# My JSON validation (10)
try:
    my_bad_json = '{"name": "David", "age": invalid}'
    my_result = json.loads(my_bad_json)
except json.JSONDecodeError as e:
    print(f"My JSON error: {e}")

# My JSON filtering (11)
my_records = [
    {"name": "David", "age": 30, "city": "Asheville"},
    {"name": "Taylor", "age": 28, "city": "Durham"},
    {"name": "Alex", "age": 25, "city": "Charlotte"}
]

my_filtered = [r for r in my_records if r["age"] > 25]
print("My filtered records:", json.dumps(my_filtered, indent=2))

# My JSON cleanup
import os
if os.path.exists("my_dog_data.json"):
    os.remove("my_dog_data.json")
