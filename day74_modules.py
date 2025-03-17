# Day 74: modules and imports for my practice

import sys
print(f"My sys module: {sys}")
print(f"My sys.version: {sys.version}")

import os
my_cwd = os.getcwd()
print(f"My working directory: {my_cwd}")

from pathlib import Path
my_path = Path.home()
print(f"My home path: {my_path}")

from datetime import datetime, timedelta
my_now = datetime.now()
my_tomorrow = my_now + timedelta(days=1)
print(f"My tomorrow: {my_tomorrow.date()}")

import json as my_json
my_data = {"name": "David", "age": 30}
