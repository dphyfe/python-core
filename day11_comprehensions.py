# Day 11: list comprehensions for my practice

# My basic list to work with
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_mountains = ["Blue Ridge", "Smoky", "Pisgah", "Craggy"]

# My first list comprehension - squares (1)
my_squares = [num * num for num in my_numbers]
print("My squared numbers:", my_squares)

# Another comprehension - doubled values (2)
my_doubled = [num * 2 for num in my_numbers]
print("My doubled numbers:", my_doubled)

# Tripling my numbers
my_tripled = [num * 3 for num in my_numbers]
print("My tripled numbers:", my_tripled)

# My comprehension with a condition - only evens (3)
my_evens = [num for num in my_numbers if num % 2 == 0]
print("My even numbers:", my_evens)

# Only odd numbers from my list (4)
my_odds = [num for num in my_numbers if num % 2 != 0]
print("My odd numbers:", my_odds)

# Numbers greater than 5 from my list
my_big_numbers = [num for num in my_numbers if num > 5]
print("My numbers greater than 5:", my_big_numbers)

# My string comprehension - uppercase mountains (5)
my_upper_mountains = [mountain.upper() for mountain in my_mountains]
print("My uppercase mountains:", my_upper_mountains)

# Lowercase mountains for my practice (6)
my_lower_mountains = [mountain.lower() for mountain in my_mountains]
print("My lowercase mountains:", my_lower_mountains)

# Getting the length of each mountain name
my_mountain_lengths = [len(mountain) for mountain in my_mountains]
print("My mountain name lengths:", my_mountain_lengths)

# My comprehension with string condition (7)
my_long_mountains = [mountain for mountain in my_mountains if len(mountain) > 5]
print("My long mountain names:", my_long_mountains)

# My comprehension with string formatting (8)
my_labels = [f"Item {i}" for i in range(1, 6)]
print("My labeled items:", my_labels)

# Another formatting example
my_mountain_labels = [f"Mountain: {m}" for m in my_mountains]
print("My mountain labels:", my_mountain_labels)

# My comprehension filtering and transforming (9)
my_big_evens = [num * 10 for num in my_numbers if num % 2 == 0 and num > 4]
print("My big even numbers times 10:", my_big_evens)

# Filtering odds and squaring them
my_odd_squares = [num * num for num in my_numbers if num % 2 != 0]
print("My squared odd numbers:", my_odd_squares)

# My words list for practice
my_words = ["hiking", "dog", "trail", "Asheville", "mountains", "blue"]

# Getting my long words (10)
my_long_words = [word for word in my_words if len(word) > 5]
print("My long words:", my_long_words)

# Short words from my list
my_short_words = [word for word in my_words if len(word) <= 5]
print("My short words:", my_short_words)

# My comprehension with conditional expression (11)
my_labels_with_status = ["even" if num % 2 == 0 else "odd" for num in my_numbers[:6]]
print("My even/odd labels:", my_labels_with_status)

# My dict comprehension (12)
my_number_dict = {num: num * num for num in range(1, 6)}
print("My number to square dict:", my_number_dict)

# Another dict comprehension
my_mountain_dict = {mountain: len(mountain) for mountain in my_mountains}
print("My mountain lengths dict:", my_mountain_dict)

# My comprehension with enumerate (13)
my_indexed_mountains = [(i, mountain) for i, mountain in enumerate(my_mountains)]
print("My indexed mountains:", my_indexed_mountains)

# My comprehension with zip (14)
my_names = ["Scout", "Luna", "Max"]
my_ages = [3, 5, 2]
my_dog_info = [(name, age) for name, age in zip(my_names, my_ages)]
print("My dog info:", my_dog_info)

# My flattening comprehension (15)
my_nested = [[1, 2], [3, 4], [5, 6]]
my_flat = [num for sublist in my_nested for num in sublist]
print("My flattened list:", my_flat)
