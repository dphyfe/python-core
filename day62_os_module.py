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
my_dir = os.path.dirname("/path/to/file.txt")
print(f"My basename: {my_base}")
print(f"My dirname: {my_dir}")

my_name, my_ext = os.path.splitext("document.txt")
print(f"My name: {my_name}, ext: {my_ext}")

for my_root, my_dirs, my_files in os.walk("my_test_dir"):
    print(f"My root: {my_root}")
    print(f"My dirs: {my_dirs}")
    print(f"My files: {my_files}")

os.rmdir("my_test_dir/sub")
os.rmdir("my_test_dir")
print("My cleanup done")

my_env = os.environ.get("PATH")
print(f"My PATH first 50 chars: {my_env[:50] if my_env else 'None'}")

my_sep = os.sep
print(f"My separator: {my_sep}")

my_user = os.path.expanduser("~")
print(f"My home: {my_user}")

# Progress: part 2/2
