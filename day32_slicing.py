# Day 32: slicing and indexing for my practice

# My basic indexing (1)
my_list = ["a", "b", "c", "d", "e"]
print(f"My first: {my_list[0]}")
print(f"My second: {my_list[1]}")
print(f"My last: {my_list[-1]}")

# My negative indexing (2)
my_list = [10, 20, 30, 40, 50]
print(f"My last: {my_list[-1]}")
print(f"My second to last: {my_list[-2]}")

# My basic slicing (3)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_first_three = my_list[0:3]
my_middle = my_list[3:6]
print(f"My first three: {my_first_three}")
print(f"My middle: {my_middle}")

# My slice without start (4)
my_last_three = my_list[:3]
my_end = my_list[7:]
print(f"My first three: {my_last_three}")
print(f"My from 7: {my_end}")

# My slice with step (5)
my_evens = my_list[::2]
my_odds = my_list[1::2]
print(f"My evens: {my_evens}")
print(f"My odds: {my_odds}")

# My reverse slice (6)
my_reversed = my_list[::-1]
my_last_three_reversed = my_list[:-4:-1]
print(f"My reversed: {my_reversed}")

# My string slicing (7)
my_text = "Hello World"
print(f"My first 5: {my_text[:5]}")
print(f"My last 5: {my_text[-5:]}")

# My slice assignment (8)
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [20, 30]
print(f"My after assignment: {my_list}")

# My slice deletion (9)
my_list = [1, 2, 3, 4, 5]
del my_list[1:3]
print(f"My after deletion: {my_list}")

# My tuple slicing (10)
my_tuple = (1, 2, 3, 4, 5)
my_slice = my_tuple[1:4]
print(f"My tuple slice: {my_slice}")

# My slice object (11)
my_slice_obj = slice(1, 4)
my_result = my_list[my_slice_obj]
print(f"My with slice object: {my_result}")

# My nested slicing (12)
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"My first row: {my_matrix[0]}")
print(f"My first two rows: {my_matrix[0:2]}")

# My range slicing (13)
my_nums = list(range(10))
my_every_other = my_nums[::2]
print(f"My every other: {my_every_other}")

# My boundary slicing (14)
my_list = [1, 2, 3]
my_beyond = my_list[0:100]
print(f"My beyond: {my_beyond}")

# My slice copy (15)
my_original = [1, 2, 3]
my_copy = my_original[:]
my_copy[0] = 99
print(f"My original: {my_original}")
print(f"My copy: {my_copy}")
