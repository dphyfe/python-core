# Day 22: CSV handling for my practice

import csv
import os

# My reading CSV (1)
my_csv_content = "name,age,city\nDavid,30,Asheville\nTaylor,28,Durham\nAlex,25,Charlotte"
with open("my_data.csv", "w") as f:
    f.write(my_csv_content)

with open("my_data.csv", "r") as my_f:
    my_reader = csv.reader(my_f)
    for my_row in my_reader:
        print(my_row)

# My DictReader (headers as keys) (2)
with open("my_data.csv", "r") as my_f:
    my_dict_reader = csv.DictReader(my_f)
    for my_row in my_dict_reader:
        print(f"My {my_row['name']} is {my_row['age']}")

# My writing CSV (3)
my_data = [
    ["name", "age", "city"],
    ["David", 30, "Asheville"],
    ["Taylor", 28, "Durham"],
    ["Alex", 25, "Charlotte"]
]

with open("my_output.csv", "w", newline="") as my_f:
    my_writer = csv.writer(my_f)
    my_writer.writerows(my_data)
print("I wrote CSV file")

# My DictWriter (4)
my_records = [
    {"name": "David", "age": 30, "city": "Asheville"},
    {"name": "Taylor", "age": 28, "city": "Durham"}
]

with open("my_records.csv", "w", newline="") as my_f:
    my_fieldnames = ["name", "age", "city"]
    my_writer = csv.DictWriter(my_f, fieldnames=my_fieldnames)
    my_writer.writeheader()
    my_writer.writerows(my_records)
