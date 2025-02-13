# Day 43: lambda functions for my practice

my_double = lambda x: x * 2
print(f"My doubled: {my_double(5)}")

my_sum = lambda a, b: a + b
print(f"My sum: {my_sum(3, 4)}")

my_nums = [1, 2, 3, 4, 5]
my_doubled = list(map(lambda x: x * 2, my_nums))
print(f"My mapped: {my_doubled}")

my_evens = list(filter(lambda x: x % 2 == 0, my_nums))
print(f"My filtered: {my_evens}")

my_words = ["apple", "pie", "zoo", "ant"]
my_sorted = sorted(my_words, key=lambda w: len(w))
print(f"My sorted: {my_sorted}")

my_pairs = [(1, 5), (2, 3), (4, 1)]
my_by_second = sorted(my_pairs, key=lambda x: x[1])
print(f"My by second: {my_by_second}")

my_max_len = max(my_words, key=lambda w: len(w))
print(f"My longest: {my_max_len}")

my_people = [{"name": "David", "age": 30}, {"name": "Taylor", "age": 28}]
my_by_age = sorted(my_people, key=lambda p: p["age"])
print(f"My by age: {my_by_age}")

my_conditional = lambda x: "even" if x % 2 == 0 else "odd"
print(f"My 4 is: {my_conditional(4)}")
print(f"My 5 is: {my_conditional(5)}")
