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
print("I wrote records CSV")

# My reading with DictReader (5)
with open("my_records.csv", "r") as my_f:
    my_reader = csv.DictReader(my_f)
    for my_row in my_reader:
        print(f"My person: {my_row['name']} from {my_row['city']}")

# My CSV with delimiter (6)
my_pipe_content = "name|age|city\nDavid|30|Asheville\nTaylor|28|Durham"
with open("my_pipe.csv", "w") as f:
    f.write(my_pipe_content)

with open("my_pipe.csv", "r") as my_f:
    my_reader = csv.reader(my_f, delimiter="|")
    for my_row in my_reader:
        print(my_row)

# My CSV with quoting (7)
my_quoted_data = [
    ["name", "description"],
    ["Item, One", "This has a comma"],
    ["Item Two", "This is normal"]
]

with open("my_quoted.csv", "w", newline="") as my_f:
    my_writer = csv.writer(my_f, quoting=csv.QUOTE_MINIMAL)
    my_writer.writerows(my_quoted_data)

with open("my_quoted.csv", "r") as my_f:
    my_reader = csv.reader(my_f)
    for my_row in my_reader:
        print(my_row)

# My processing CSV data (8)
with open("my_data.csv", "r") as my_f:
    my_reader = csv.DictReader(my_f)
    my_people_over_25 = [row for row in my_reader if int(row["age"]) > 25]
    print(f"My people over 25: {len(my_people_over_25)}")

# My CSV column extraction (9)
with open("my_data.csv", "r") as my_f:
    my_reader = csv.DictReader(my_f)
    my_names = [row["name"] for row in my_reader]
    print("My names:", my_names)

# My CSV appending (10)
with open("my_data.csv", "a", newline="") as my_f:
    my_writer = csv.writer(my_f)
    my_writer.writerow(["Scout", 3, "Asheville"])

print("I appended to CSV")

# Cleanup my test files
for my_file in ["my_data.csv", "my_output.csv", "my_records.csv", "my_pipe.csv", "my_quoted.csv"]:
    if os.path.exists(my_file):
        os.remove(my_file)

# Progress: part 2/2
