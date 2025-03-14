# Day 71: virtual environments for my practice

import sys
import os

my_version = sys.version
print(f"My Python version: {my_version}")

my_executable = sys.executable
print(f"My Python executable: {my_executable}")

my_prefix = sys.prefix
print(f"My prefix: {my_prefix}")

my_base_prefix = sys.base_prefix
print(f"My base prefix: {my_base_prefix}")

my_in_venv = sys.prefix != sys.base_prefix
print(f"My in virtual env: {my_in_venv}")

my_path = sys.path
print(f"My sys.path entries: {len(my_path)}")
for my_entry in my_path[:3]:
    print(f"  My path: {my_entry}")

import site
my_packages = site.getsitepackages()
print(f"My site packages: {my_packages}")

my_user_site = site.getusersitepackages()
print(f"My user site: {my_user_site}")

print("\nMy venv creation commands:")
print("  python -m venv my_env")
print("  .\\my_env\\Scripts\\activate  (Windows)")
print("  source my_env/bin/activate  (Unix)")

print("\nMy venv workflow:")
print("  1. python -m venv my_env")
print("  2. activate my_env")
print("  3. pip install package_name")
print("  4. pip freeze > requirements.txt")
print("  5. deactivate")

my_platform = sys.platform
print(f"\nMy platform: {my_platform}")

my_virtual_env = os.environ.get('VIRTUAL_ENV')
print(f"My VIRTUAL_ENV: {my_virtual_env}")

print("\nMy venv best practices:")
print("  - Always use venv for projects")
print("  - Keep requirements.txt updated")
print("  - Don't commit venv to git")
print("  - Use .gitignore for venv/")
