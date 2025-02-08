# Day 39: any all sum min max for my practice

# My any function (1)
my_list = [False, False, True, False]
print(f"My any: {any(my_list)}")

my_all_false = [False, False, False]
print(f"My any all false: {any(my_all_false)}")

# My all function (2)
my_all_true = [True, True, True]
print(f"My all: {all(my_all_true)}")

my_mixed = [True, True, False]
print(f"My all mixed: {all(my_mixed)}")

# My sum function (3)
my_nums = [1, 2, 3, 4, 5]
print(f"My sum: {sum(my_nums)}")

# My sum with start (4)
my_sum_100 = sum(my_nums, 100)
print(f"My sum with start: {my_sum_100}")

# My min function (5)
print(f"My min: {min(my_nums)}")

my_words = ["zebra", "apple", "monkey"]
print(f"My min word: {min(my_words)}")

# My max function (6)
print(f"My max: {max(my_nums)}")
print(f"My max word: {max(my_words)}")

# My min with key (7)
my_by_len = min(my_words, key=len)
print(f"My min by length: {my_by_len}")

# My max with key (8)
my_people = [{"name": "David", "age": 30}, {"name": "Taylor", "age": 28}]
my_oldest = max(my_people, key=lambda p: p["age"])
print(f"My oldest: {my_oldest}")

# My any with condition (9)
my_values = [1, 2, 3, 4, 5]
my_has_even = any(x % 2 == 0 for x in my_values)
print(f"My has even: {my_has_even}")

# My all with condition (10)
my_all_positive = all(x > 0 for x in my_values)
print(f"My all positive: {my_all_positive}")

# My empty lists (11)
print(f"My any empty: {any([])}")
print(f"My all empty: {all([])}")

# My sum floats (12)
my_floats = [1.5, 2.5, 3.0]

# Progress: part 3/4
