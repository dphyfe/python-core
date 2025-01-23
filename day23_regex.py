# Day 23: regular expressions for my practice

import re

# My basic regex match (1)
my_pattern = r"hello"
my_text = "hello world"
my_match = re.search(my_pattern, my_text)
if my_match:
    print(f"My match found: {my_match.group()}")

# My matching at start (2)
my_pattern = r"^hello"
my_text1 = "hello world"
my_text2 = "say hello"
print(f"My text1 matches: {bool(re.search(my_pattern, my_text1))}")
print(f"My text2 matches: {bool(re.search(my_pattern, my_text2))}")

# My character classes (3)
my_pattern = r"[aeiou]"
my_text = "hello"
my_matches = re.findall(my_pattern, my_text)
print(f"My vowels: {my_matches}")

# My digit matching (4)
my_pattern = r"\d"
my_text = "I have 3 dogs and 2 cats"
my_digits = re.findall(my_pattern, my_text)
print(f"My digits: {my_digits}")

# My word character matching (5)
my_pattern = r"\w+"
my_text = "Hello-world_123"
my_words = re.findall(my_pattern, my_text)
print(f"My words: {my_words}")

# My finding all matches (6)
my_pattern = r"[0-9]+"
my_text = "I scored 95, 87, and 92 points"
my_numbers = re.findall(my_pattern, my_text)
print(f"My numbers: {my_numbers}")

# My capturing groups (7)
my_pattern = r"(\w+)@(\w+)\.(\w+)"
my_email = "david@example.com"
my_match = re.search(my_pattern, my_email)
if my_match:
    print(f"My username: {my_match.group(1)}")
    print(f"My domain: {my_match.group(2)}")

# My optional patterns (8)
