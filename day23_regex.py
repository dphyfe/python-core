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
my_pattern = r"colou?r"
print(f"My 'color' matches: {bool(re.search(my_pattern, 'color'))}")
print(f"My 'colour' matches: {bool(re.search(my_pattern, 'colour'))}")

# My repetition patterns (9)
my_pattern = r"a{3}"
my_text1 = "aaa"
my_text2 = "aa"
print(f"My 'aaa' matches: {bool(re.search(my_pattern, my_text1))}")
print(f"My 'aa' matches: {bool(re.search(my_pattern, my_text2))}")

# My alternation (10)
my_pattern = r"dog|cat|bird"
my_animals = ["dog", "cat", "fish", "bird"]
for animal in my_animals:
    print(f"My '{animal}' matches: {bool(re.search(my_pattern, animal))}")

# My string replacement (11)
my_pattern = r"\d+"
my_text = "I have 2 dogs and 1 cat"
my_result = re.sub(my_pattern, "X", my_text)
print(f"My replaced: {my_result}")

# My substitution with groups (12)
my_pattern = r"(\d+)/(\d+)/(\d+)"
my_date = "01/15/2025"
my_result = re.sub(my_pattern, r"\3-\1-\2", my_date)
print(f"My reformatted date: {my_result}")

# My splitting with regex (13)
my_pattern = r"[,;]"
my_text = "apple,banana;cherry,date"
my_result = re.split(my_pattern, my_text)
print(f"My split: {my_result}")

# My case-insensitive matching (14)
my_pattern = r"HELLO"
my_text = "hello world"
my_match = re.search(my_pattern, my_text, re.IGNORECASE)
print(f"My case-insensitive match: {bool(my_match)}")

# My multiline matching (15)
my_pattern = r"^line"
my_text = "start\nline 2\nline 3"
my_matches = re.findall(my_pattern, my_text, re.MULTILINE)
print(f"My multiline matches: {len(my_matches)}")

# Progress: part 2/2
