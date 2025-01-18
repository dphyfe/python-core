# Day 18: working with lists and data structures for my practice

# My list operations (1)
my_numbers = [1, 2, 3, 4, 5]
print("My list:", my_numbers)

# My list slicing (2)
my_first_three = my_numbers[:3]
my_last_two = my_numbers[-2:]
my_middle = my_numbers[1:4]
print("First three:", my_first_three)
print("Last two:", my_last_two)
print("Middle:", my_middle)

# My list methods - append, extend, insert (3)
my_hobbies = ["hiking", "coding"]
my_hobbies.append("reading")
print("After append:", my_hobbies)

my_hobbies.extend(["gaming", "cooking"])
print("After extend:", my_hobbies)

my_hobbies.insert(1, "writing")
print("After insert:", my_hobbies)

# My list pop and remove (4)
my_items = [10, 20, 30, 40, 50]
my_popped = my_items.pop()
print("Popped:", my_popped)
print("After pop:", my_items)

my_items.remove(20)
print("After remove:", my_items)

# My list sorting (5)
my_scores = [85, 92, 78, 95, 88]
my_sorted = sorted(my_scores)
print("Original:", my_scores)
print("Sorted:", my_sorted)

my_scores.sort(reverse=True)
print("Sorted descending:", my_scores)

# My list with strings (6)
my_words = ["python", "apple", "zebra", "monkey"]
my_sorted_words = sorted(my_words)
print("Sorted words:", my_sorted_words)

my_sorted_by_length = sorted(my_words, key=len)
print("Sorted by length:", my_sorted_by_length)

# My nested lists (7)
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("My matrix:", my_matrix)
print("First row:", my_matrix[0])
print("Item [1][2]:", my_matrix[1][2])

# My list iteration (8)
my_fruits = ["apple", "banana", "cherry"]
for fruit in my_fruits:
    print(f"- {fruit}")

for i, fruit in enumerate(my_fruits):
    print(f"{i}: {fruit}")

# My list with zip (9)
my_names = ["David", "Taylor", "Alex"]
my_ages = [30, 28, 25]
for name, age in zip(my_names, my_ages):
    print(f"{name} is {age}")

# My list copy (10)
my_original = [1, 2, 3]
my_shallow_copy = my_original.copy()
my_shallow_copy[0] = 99
print("Original:", my_original)
print("Copy:", my_shallow_copy)

# My list reversal (11)
my_reverse = [1, 2, 3, 4, 5]
my_reversed = list(reversed(my_reverse))
print("Reversed:", my_reversed)

my_reverse.reverse()
print("After reverse():", my_reverse)

# My list count and index (12)
my_data = [1, 2, 3, 2, 4, 2, 5]
print("Count of 2:", my_data.count(2))
print("Index of 3:", my_data.index(3))

# My list cleaning and filtering (13)
my_with_nones = [1, None, 2, None, 3]
my_clean = [x for x in my_with_nones if x is not None]
print("Cleaned:", my_clean)

my_with_zeros = [0, 1, 0, 2, 0, 3]
my_no_zeros = [x for x in my_with_zeros if x != 0]
print("No zeros:", my_no_zeros)

# My list flattening (14)
my_nested = [[1, 2], [3, 4], [5, 6]]
my_flat = [item for sublist in my_nested for item in sublist]
print("Flattened:", my_flat)

# My list as stack (LIFO) (15)
my_stack = []
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
print("Stack:", my_stack)
my_popped_item = my_stack.pop()
print("Popped:", my_popped_item)
print("After pop:", my_stack)

# My list methods summary (16)
my_test_list = [3, 1, 4, 1, 5, 9, 2, 6]
print("Length:", len(my_test_list))
print("Min:", min(my_test_list))
print("Max:", max(my_test_list))
print("Sum:", sum(my_test_list))
print("Count 1s:", my_test_list.count(1))

# Progress: part 3/3
