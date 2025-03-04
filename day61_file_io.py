# Day 61: file I/O modes for my practice

with open("my_test.txt", "w") as f:
    f.write("My first line\n")
    f.write("My second line\n")
print("My file written")

with open("my_test.txt", "r") as f:
    my_content = f.read()
    print(f"My content:\n{my_content}")

with open("my_test.txt", "r") as f:
    my_lines = f.readlines()
    print(f"My lines: {my_lines}")

with open("my_test.txt", "a") as f:
    f.write("My appended line\n")
print("My line appended")

with open("my_test.txt", "r") as f:
    for my_line in f:
        print(f"My line: {my_line.strip()}")

try:
    with open("nonexistent.txt", "r") as f:
        pass
except FileNotFoundError:
    print("My file not found")

with open("my_binary.bin", "wb") as f:
    my_data = bytes([1, 2, 3, 4, 5])
    f.write(my_data)

with open("my_binary.bin", "rb") as f:
    my_read = f.read()
    print(f"My binary: {list(my_read)}")

with open("my_test.txt", "r") as f:
    my_first_line = f.readline()
    print(f"My first line: {my_first_line.strip()}")

with open("my_pos.txt", "w+") as f:
    f.write("My test")
    f.seek(0)
    my_content = f.read()
    print(f"My r+w content: {my_content}")

import os
os.remove("my_test.txt")
os.remove("my_binary.bin")
os.remove("my_pos.txt")
print("My cleanup complete")
