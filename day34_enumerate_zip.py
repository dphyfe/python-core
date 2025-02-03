# Day 34: enumerate and zip for my practice

# My enumerate basics (1)
my_fruits = ["apple", "banana", "cherry"]
for my_idx, my_fruit in enumerate(my_fruits):
    print(f"My {my_idx}: {my_fruit}")

# My enumerate with start (2)
for my_idx, my_fruit in enumerate(my_fruits, start=1):
    print(f"My {my_idx}: {my_fruit}")

# My enumerate in list (3)
my_indexed = list(enumerate(my_fruits))
print(f"My indexed: {my_indexed}")

# My enumerate unpacking (4)
my_items = ["x", "y", "z"]
for my_i, my_item in enumerate(my_items):
    print(f"My position {my_i}: {my_item}")

# My zip basics (5)
my_names = ["David", "Taylor", "Alex"]
my_ages = [30, 28, 25]
for my_name, my_age in zip(my_names, my_ages):
    print(f"My {my_name}: {my_age}")

# My zip with lists (6)
my_zipped = list(zip(my_names, my_ages))
print(f"My zipped: {my_zipped}")

# My zip multiple (7)
my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = [10, 20, 30]
for my_a, my_b, my_c in zip(my_list1, my_list2, my_list3):
    print(f"My {my_a}, {my_b}, {my_c}")

# My zip unequal length (8)
my_short = [1, 2]
my_long = ["a", "b", "c", "d"]
my_result = list(zip(my_short, my_long))
print(f"My zipped unequal: {my_result}")

# My zip unpack (9)
my_pairs = [(1, "a"), (2, "b"), (3, "c")]
my_nums, my_letters = zip(*my_pairs)
print(f"My numbers: {my_nums}")
print(f"My letters: {my_letters}")

# My enumerate with zip (10)
for my_idx, (my_name, my_age) in enumerate(zip(my_names, my_ages)):
    print(f"My {my_idx}: {my_name} ({my_age})")

# My enumerate dict items (11)
my_dict = {"a": 1, "b": 2, "c": 3}
for my_idx, (my_key, my_val) in enumerate(my_dict.items()):
    print(f"My {my_idx}: {my_key}={my_val}")

# My zip dict (12)
my_keys = ["name", "age", "city"]
my_values = ["David", 30, "Asheville"]
my_zipped_dict = dict(zip(my_keys, my_values))
print(f"My dict from zip: {my_zipped_dict}")

# My reversed with enumerate (13)
my_items = ["a", "b", "c"]
for my_idx, my_item in enumerate(reversed(my_items)):
    print(f"My {my_idx}: {my_item}")

# My transpose with zip (14)
my_matrix = [[1, 2, 3], [4, 5, 6]]
my_transposed = list(zip(*my_matrix))
print(f"My transposed: {my_transposed}")

# My enumerate skip (15)
for my_idx, my_item in enumerate(my_fruits):
    if my_idx > 0:
        print(f"My {my_idx}: {my_item}")
