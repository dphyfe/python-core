# Day 35: list and dict comprehensions for my practice

# My list comprehension (1)
my_squared = [x**2 for x in range(5)]
print(f"My squared: {my_squared}")

# My filtered comprehension (2)
my_evens = [x for x in range(10) if x % 2 == 0]
print(f"My evens: {my_evens}")

# My conditional comprehension (3)
my_items = ["odd" if x % 2 else "even" for x in range(5)]
print(f"My odd/even: {my_items}")

# My nested comprehension (4)
my_matrix = [[y for y in range(3)] for x in range(3)]
print(f"My matrix: {my_matrix}")

# My flattening (5)
my_nested = [[1, 2], [3, 4], [5, 6]]
my_flat = [item for sublist in my_nested for item in sublist]
print(f"My flat: {my_flat}")

# My dict comprehension (6)
my_dict = {x: x**2 for x in range(5)}
print(f"My dict squares: {my_dict}")

# My dict from lists (7)
my_keys = ["a", "b", "c"]
my_values = [1, 2, 3]
my_dict = {k: v for k, v in zip(my_keys, my_values)}
print(f"My zipped dict: {my_dict}")

# My filtering dict (8)
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
my_filtered = {k: v for k, v in my_dict.items() if v > 2}
print(f"My filtered dict: {my_filtered}")

# My transforming dict (9)
my_data = {"name": "david", "city": "asheville"}
my_upper = {k: v.upper() for k, v in my_data.items()}
print(f"My upper dict: {my_upper}")

# My inverting dict (10)
my_dict = {"a": 1, "b": 2, "c": 3}
my_inverted = {v: k for k, v in my_dict.items()}
print(f"My inverted: {my_inverted}")

# My comprehension with condition (11)
my_text = "hello"
my_vowels = [c for c in my_text if c in "aeiou"]
print(f"My vowels: {my_vowels}")

# My list to dict comprehension (12)
my_pairs = [(1, "a"), (2, "b"), (3, "c")]
my_d = {k: v for k, v in my_pairs}
print(f"My from pairs: {my_d}")

# My set comprehension (13)
my_set = {x % 3 for x in range(10)}
print(f"My set: {my_set}")

# My comprehension performance (14)
my_big = [x for x in range(1000) if x % 2 == 0]
print(f"My big list length: {len(my_big)}")

# My nested filtering (15)
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_gt_5 = [item for row in my_matrix for item in row if item > 5]
print(f"My greater than 5: {my_gt_5}")

# Progress: part 4/4
