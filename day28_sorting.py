# Day 28: sorting and sorted for my practice

# My basic sorted (1)
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_sorted = sorted(my_numbers)
print(f"My sorted: {my_sorted}")

# My reverse sort (2)
my_reverse = sorted(my_numbers, reverse=True)
print(f"My reverse: {my_reverse}")

# My sorting strings (3)
my_words = ["zebra", "apple", "monkey", "dog"]
my_sorted_words = sorted(my_words)
print(f"My sorted words: {my_sorted_words}")

# My sorting by length (4)
my_lengths = sorted(my_words, key=len)
print(f"My by length: {my_lengths}")

# My list sort (modifies in place) (5)
my_list = [3, 1, 4, 1, 5]
my_list.sort()
print(f"My sorted list: {my_list}")

# My sorting dicts (6)
my_people = [
    {"name": "David", "age": 30},
    {"name": "Taylor", "age": 28},
    {"name": "Alex", "age": 25}
]
my_by_age = sorted(my_people, key=lambda x: x["age"])
print(f"My by age: {my_by_age}")

# My sorting with custom key (7)
my_words = ["Hello", "world", "PYTHON"]
my_by_lower = sorted(my_words, key=str.lower)
print(f"My case-insensitive: {my_by_lower}")

# My sorting tuples (8)
my_coords = [(3, 4), (1, 2), (2, 1)]
my_sorted_coords = sorted(my_coords)
print(f"My sorted tuples: {my_sorted_coords}")

# My sorting stability (9)
my_items = [(1, "a"), (2, "b"), (1, "c")]
my_stable = sorted(my_items, key=lambda x: x[0])
print(f"My stable sort: {my_stable}")

# My multiple criteria (10)
my_data = sorted(my_people, key=lambda x: (x["age"], x["name"]))
print(f"My multi-sort: {my_data}")

# My reverse keys (11)
my_reverse_age = sorted(my_people, key=lambda x: x["age"], reverse=True)
print(f"My oldest first: {my_reverse_age}")

# My sorted performance (12)
my_big_list = list(range(1000, 0, -1))
my_result = sorted(my_big_list)
print(f"My sorted big list first 5: {my_result[:5]}")

# My string with numbers (13)
my_files = ["file1.txt", "file10.txt", "file2.txt"]
my_natural_sort = sorted(my_files, key=lambda x: x.replace("file", "").replace(".txt", ""), type=int)
print(f"My files sorted: {my_files}")

# My case sensitivity (14)
my_mixed_case = ["apple", "Apple", "APPLE"]
my_sorted_case = sorted(my_mixed_case)
print(f"My case sensitive: {my_sorted_case}")

# My custom comparator (15)
my_items = ["apple", "pie", "zoo", "app"]
my_by_first_last = sorted(my_items, key=lambda x: (x[0], x[-1]))
print(f"My by first/last char: {my_by_first_last}")
