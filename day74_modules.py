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
my_string = my_json.dumps(my_data)
print(f"My JSON: {my_string}")

from collections import defaultdict, Counter
my_dd = defaultdict(int)
my_dd["count"] += 1
print(f"My defaultdict: {dict(my_dd)}")

my_words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
my_counter = Counter(my_words)
print(f"My counter: {my_counter}")

import math
print(f"My pi: {math.pi}")
print(f"My sqrt(16): {math.sqrt(16)}")

import random
my_rand = random.randint(1, 10)
print(f"My random: {my_rand}")

import re
my_match = re.search(r'\d+', 'My number is 42')
if my_match:
    print(f"My match: {my_match.group()}")

print(f"\nMy sys.path entries: {len(sys.path)}")
print(f"My first path: {sys.path[0]}")

print("\nMy import patterns:")
print("  import module")
print("  from module import name")
print("  from module import name1, name2")
print("  from module import *  # avoid")
print("  import module as alias")

print("\nMy module search order:")
print("  1. Current directory")
print("  2. PYTHONPATH")
print("  3. Standard library")
print("  4. Site-packages")

# Progress: part 3/3
