# Day 38: any all sum min max for my practice

# My any basics (1)
my_list = [False, False, True, False]
print(f"My any: {any(my_list)}")

# My all basics (2)
my_list2 = [True, True, True]
print(f"My all: {all(my_list2)}")

# My any with generator (3)
my_nums = [2, 4, 6, 7, 8]
my_has_odd = any(x % 2 for x in my_nums)
print(f"My has odd: {my_has_odd}")

# My all with generator (4)
my_all_even = all(x % 2 == 0 for x in my_nums)
print(f"My all even: {my_all_even}")

# My sum basics (5)
my_nums = [1, 2, 3, 4, 5]
my_total = sum(my_nums)
print(f"My sum: {my_total}")

# My sum with start (6)
my_sum_plus = sum(my_nums, 10)
print(f"My sum plus 10: {my_sum_plus}")

# My min max (7)
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"My min: {min(my_numbers)}")
print(f"My max: {max(my_numbers)}")

# My min max with strings (8)
my_words = ["apple", "banana", "cherry"]
print(f"My min word: {min(my_words)}")
print(f"My max word: {max(my_words)}")

# My any with list (9)
my_values = [0, 0, 0, 1]
print(f"My any nonzero: {any(my_values)}")

# My all empty (10)
my_empty = []
print(f"My all empty: {all(my_empty)}")
print(f"My any empty: {any(my_empty)}")

# My sum floats (11)
my_floats = [1.5, 2.5, 3.0]
print(f"My float sum: {sum(my_floats)}")

# My min max with key (12)
my_words = ["a", "bb", "ccc"]
print(f"My min by length: {min(my_words, key=len)}")
print(f"My max by length: {max(my_words, key=len)}")

# My any with dict (13)
my_dict = {"a": False, "b": False, "c": True}
print(f"My any dict values: {any(my_dict.values())}")

# My sum dict values (14)
my_data = {"a": 1, "b": 2, "c": 3}
print(f"My dict sum: {sum(my_data.values())}")

# My combined (15)
my_nums = [1, 2, 3, 4, 5]
my_has_even = any(x % 2 == 0 for x in my_nums)
my_all_positive = all(x > 0 for x in my_nums)
my_average = sum(my_nums) / len(my_nums)
print(f"My has even: {my_has_even}, all positive: {my_all_positive}, avg: {my_average}")
