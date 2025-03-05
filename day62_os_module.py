# Day 62: os module for my practice

import os

my_cwd = os.getcwd()
print(f"My cwd: {my_cwd}")

os.makedirs("my_test_dir/sub", exist_ok=True)
print("My directories created")

my_files = os.listdir(".")
print(f"My files count: {len(my_files)}")

my_path = os.path.join("my_test_dir", "file.txt")
print(f"My joined path: {my_path}")

print(f"My exists: {os.path.exists('my_test_dir')}")
print(f"My is_dir: {os.path.isdir('my_test_dir')}")
print(f"My is_file: {os.path.isfile('my_test_dir')}")

my_abs = os.path.abspath("my_test_dir")
print(f"My absolute: {my_abs}")

my_base = os.path.basename("/path/to/file.txt")
