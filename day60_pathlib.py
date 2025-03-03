# Day 60: pathlib for my practice

from pathlib import Path

my_path = Path("test.txt")
print(f"My path: {my_path}")
print(f"My absolute: {my_path.absolute()}")

my_file = Path("data") / "config.json"
print(f"My joined: {my_file}")

my_home = Path.home()
print(f"My home: {my_home}")

my_cwd = Path.cwd()
print(f"My cwd: {my_cwd}")

my_path = Path("document.txt")
