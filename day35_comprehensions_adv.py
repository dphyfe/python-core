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
