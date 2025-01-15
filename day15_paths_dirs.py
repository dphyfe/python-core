# Day 15: working with paths and directories for my practice

import os
from pathlib import Path

# My current working directory (1)
my_cwd = os.getcwd()
print("My current directory:", my_cwd)

# My path joining (2)
my_path = os.path.join("python-core", "day15_test.txt")
print("My joined path:", my_path)

# Another path join
my_data_path = os.path.join("data", "files", "notes.txt")
print("My data path:", my_data_path)

# My path splitting (3)
my_directory, my_filename = os.path.split(my_path)
print("My directory:", my_directory)
print("My filename:", my_filename)

# My path parts (4)
my_base, my_ext = os.path.splitext("day15_paths.py")
print("My base:", my_base)
print("My extension:", my_ext)

# My path existence checks (5)
print("Does python-core exist?", os.path.exists("python-core"))
print("Does fake-dir exist?", os.path.exists("fake-dir"))

# My file vs directory checks (6)
if os.path.exists("python-core"):
    print("Is python-core a dir?", os.path.isdir("python-core"))
    print("Is python-core a file?", os.path.isfile("python-core"))

# My absolute path (7)
my_abs_path = os.path.abspath(".")
print("My absolute path:", my_abs_path)


# My Path object (pathlib) - easier to use! (8)
my_pathlib_path = Path(".")
print("My pathlib current:", my_pathlib_path.absolute())

# My pathlib file path
my_file_path = Path("python-core") / "day01_basics.py"
print("My pathlib file:", my_file_path)

# My pathlib existence (9)
print("My pathlib exists?", my_file_path.exists())
print("My fake path exists?", (Path("fake") / "file.txt").exists())

# My pathlib is_file and is_dir (10)
my_dir_path = Path("python-core")
print("Is python-core a dir?", my_dir_path.is_dir())
print("Is python-core a file?", my_dir_path.is_file())

# My pathlib parts (11)
my_parts = my_file_path.parts
print("My path parts:", my_parts)

my_name = my_file_path.name
print("My file name:", my_name)

my_stem = my_file_path.stem
print("My file stem:", my_stem)

my_suffix = my_file_path.suffix
print("My file suffix:", my_suffix)

# My pathlib parent (12)
my_parent = my_file_path.parent
print("My file parent:", my_parent)

# My pathlib glob (13)
print("My .py files in python-core:")
my_py_files = list(Path("python-core").glob("*.py"))
for py_file in my_py_files[:5]:  # first 5
    print("-", py_file.name)

# My pathlib read and write (14)
my_test_file = Path("my_test.txt")
my_test_file.write_text("My pathlib content\\n", encoding="utf-8")
print("I wrote to my test file")

my_content = my_test_file.read_text(encoding="utf-8")
print("My file content:", my_content.strip())

# Clean up my test file
if my_test_file.exists():
    my_test_file.unlink()
    print("I removed my test file")

# My home directory (15)
my_home = Path.home()
print("My home directory:", my_home)
