# Day 36: map filter reduce for my practice

# My map basics (1)
my_nums = [1, 2, 3, 4, 5]
my_doubled = list(map(lambda x: x * 2, my_nums))
print(f"My doubled: {my_doubled}")

# My map with function (2)
def my_triple(x):
    return x * 3

my_tripled = list(map(my_triple, my_nums))
print(f"My tripled: {my_tripled}")

# My filter basics (3)
my_filtered = list(filter(lambda x: x > 2, my_nums))
print(f"My filtered: {my_filtered}")

# My filter with function (4)
def my_is_even(x):
    return x % 2 == 0

my_evens = list(filter(my_is_even, my_nums))
print(f"My evens: {my_evens}")

# My reduce import (5)
from functools import reduce

my_product = reduce(lambda a, b: a * b, my_nums)
print(f"My product: {my_product}")

# My reduce sum (6)
my_sum = reduce(lambda a, b: a + b, my_nums)
print(f"My sum: {my_sum}")

# My map strings (7)
my_words = ["apple", "banana", "cherry"]
my_lengths = list(map(len, my_words))
print(f"My lengths: {my_lengths}")

# My filter strings (8)
my_long_words = list(filter(lambda w: len(w) > 5, my_words))
print(f"My long: {my_long_words}")

# My chaining (9)
my_chain = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, my_nums)))
print(f"My chained: {my_chain}")

# My vs comprehension (10)
my_comp = [x * 2 for x in my_nums]
my_map = list(map(lambda x: x * 2, my_nums))
print(f"My same: {my_comp == my_map}")

# My reduce with initial (11)
my_result = reduce(lambda a, b: a + b, my_nums, 100)
print(f"My sum with initial: {my_result}")

# My map multiple lists (12)
my_a = [1, 2, 3]
my_b = [4, 5, 6]
my_sums = list(map(lambda x, y: x + y, my_a, my_b))
print(f"My sums: {my_sums}")

# My filter objects (13)
my_people = [{"name": "David", "age": 30}, {"name": "Taylor", "age": 28}]
my_over_25 = list(filter(lambda p: p["age"] > 25, my_people))
print(f"My over 25: {my_over_25}")

# My map dict (14)
my_keys = ["a", "b", "c"]
my_dict = dict(zip(my_keys, map(lambda x: x**2, range(1, 4))))
print(f"My dict: {my_dict}")

# My functional style (15)
my_result = reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, map(lambda x: x * 2, my_nums)))
print(f"My functional: {my_result}")
