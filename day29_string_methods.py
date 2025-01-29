# Day 29: string methods for my practice

# My split method (1)
my_text = "apple,banana,cherry"
my_parts = my_text.split(",")
print(f"My split: {my_parts}")

# My split default (whitespace) (2)
my_words = "hello world python"
my_split = my_words.split()
print(f"My split words: {my_split}")

# My join method (3)
my_list = ["hello", "world", "python"]
my_joined = " ".join(my_list)
print(f"My joined: {my_joined}")

# My join with dash (4)
my_items = ["a", "b", "c"]
my_dashed = "-".join(my_items)
print(f"My dashed: {my_dashed}")

# My strip method (5)
my_messy = "  hello world  \n"
my_clean = my_messy.strip()
print(f"My stripped: '{my_clean}'")

# My lstrip and rstrip (6)
my_text = ">>>hello<<<"
my_left = my_text.lstrip(">")
my_right = my_text.rstrip("<")
print(f"My lstrip: {my_left}")
print(f"My rstrip: {my_right}")

# My replace method (7)
my_text = "hello world"
my_replaced = my_text.replace("world", "python")
print(f"My replaced: {my_replaced}")

# My replace count (8)
my_multi = "aaa"
my_result = my_multi.replace("a", "b", 2)
print(f"My replaced 2: {my_result}")

# My find method (9)
my_text = "hello world"
my_index = my_text.find("world")
print(f"My find: {my_index}")

# My startswith and endswith (10)
my_text = "hello.py"
print(f"My startswith: {my_text.startswith('hello')}")
print(f"My endswith: {my_text.endswith('.py')}")

# My upper and lower (11)
my_text = "Hello World"
print(f"My upper: {my_text.upper()}")
print(f"My lower: {my_text.lower()}")

# My capitalize (12)
my_text = "hello world"
my_cap = my_text.capitalize()
print(f"My capitalized: {my_cap}")

# My title (13)
my_text = "hello world python"
my_title = my_text.title()
print(f"My title: {my_title}")

# My count method (14)
my_text = "apple banana apple cherry apple"
my_count = my_text.count("apple")
print(f"My count: {my_count}")

# My isdigit and isalpha (15)
print(f"My '123' isdigit: {'123'.isdigit()}")
print(f"My 'abc' isalpha: {'abc'.isalpha()}")
