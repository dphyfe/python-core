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
