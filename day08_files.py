# Day 08: writing and reading files for my practice

# My note file path
note_path = "day08_note.txt"

# Write my first note (1)
with open(note_path, "w", encoding="utf-8") as file:
    file.write("Learning Python in Asheville.\n")
    file.write("Taking small steps each day.\n")
    file.write("Remember to walk the dogs.\n")

print("I wrote my note to", note_path)

# Append another line to my note (2)
with open(note_path, "a", encoding="utf-8") as file:
    file.write("Add a reminder to drink water.\n")

print("I appended to my note")

# Append one more reminder
with open(note_path, "a", encoding="utf-8") as file:
    file.write("Check the weather for hiking.\n")

# Read my note back (3)
with open(note_path, "r", encoding="utf-8") as file:
    content = file.read()

print("My note content:\n" + content)

# Read my lines into a list (4)
with open(note_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
print("I have", len(lines), "lines in my note")

# Print each line from my list
print("My lines one by one:")
for line in lines:
    print("  " + line.strip())

# Strip newline characters from my lines (5)
clean_lines = []
for line in lines:
    clean_lines.append(line.strip())
print("My clean lines:", clean_lines)

# Write a list of my activities to another file (6)
list_path = "day08_list.txt"
my_activities = ["hiking", "coding", "reading", "walking dogs"]
with open(list_path, "w", encoding="utf-8") as file:
    for activity in my_activities:
        file.write(activity + "\n")
print("I wrote my activities to", list_path)

# Read back my list file (7)
with open(list_path, "r", encoding="utf-8") as file:
    list_content = file.read()
print("My list file content:\n" + list_content)

# Write my mountains to a file
mountain_path = "day08_mountains.txt"
my_mountains = ["Blue Ridge", "Smoky", "Pisgah"]
with open(mountain_path, "w", encoding="utf-8") as file:
    file.write("My favorite mountains:\n")
    for mountain in my_mountains:
        file.write("- " + mountain + "\n")
print("I wrote my mountains to", mountain_path)

# Read my mountains back
with open(mountain_path, "r", encoding="utf-8") as file:
    mountains_content = file.read()
print(mountains_content)

# Check existence using try/except for my practice (8)
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        missing_content = file.read()
    print(missing_content)
except FileNotFoundError:
    print("I tried to read missing.txt but it's not here, which is expected.")

# Try another missing file
try:
    with open("not_here.txt", "r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError:
    print("I also tried not_here.txt and it's missing too.")

# Append and read my list file again to see change (9)
with open(list_path, "a", encoding="utf-8") as file:
    file.write("cook dinner\n")
with open(list_path, "r", encoding="utf-8") as file:
    print("My updated list file:\n" + file.read())

# Write numbers to a file for my practice
numbers_path = "day08_numbers.txt"
with open(numbers_path, "w", encoding="utf-8") as file:
    for i in range(1, 6):
        file.write("Number " + str(i) + "\n")
print("I wrote numbers to", numbers_path)

# Read my numbers file line by line
print("My numbers file:")
with open(numbers_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Create a file with my dog names
dog_path = "day08_dogs.txt"
with open(dog_path, "w", encoding="utf-8") as file:
    file.write("Scout\n")
    file.write("Luna\n")

print("I created my dogs file")

# Read my dogs file
with open(dog_path, "r", encoding="utf-8") as file:
    dog_lines = file.readlines()
print("My dogs:", [name.strip() for name in dog_lines])

# Overwrite my dogs file with more info
with open(dog_path, "w", encoding="utf-8") as file:
    file.write("My dogs:\n")
    file.write("1. Scout - playful\n")
    file.write("2. Luna - calm\n")

# Read my updated dogs file
with open(dog_path, "r", encoding="utf-8") as file:
    print("\nMy updated dogs file:\n" + file.read())

# Write a simple log entry
log_path = "day08_log.txt"
with open(log_path, "w", encoding="utf-8") as file:
    file.write("2025-01-08: Started learning file I/O\n")

# Append more log entries
with open(log_path, "a", encoding="utf-8") as file:
    file.write("2025-01-08: Practiced reading and writing\n")
    file.write("2025-01-08: Tried append mode\n")

print("I created my log file")

# Read my complete log
with open(log_path, "r", encoding="utf-8") as file:
    print("\nMy log:\n" + file.read())

# Progress: part 2/2
