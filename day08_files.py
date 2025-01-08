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
