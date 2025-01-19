# Day 19: exceptions and error handling patterns for my practice

# My try-except basics (1)
try:
    my_result = 10 / 0
except ZeroDivisionError:
    print("My error: cannot divide by zero")

# Another example
try:
    my_number = int("not a number")
except ValueError:
    print("My error: invalid number string")

# My multiple except blocks (2)
try:
    my_data = [1, 2, 3]
    my_value = my_data[10]
except IndexError:
    print("My error: index out of range")
except TypeError:
    print("My error: type error")

# My except for multiple errors (3)
try:
    my_dict = {"name": "David"}
    my_age = my_dict["age"]
except (KeyError, TypeError):
    print("My error: key or type problem")

# My except-else pattern (4)
try:
    my_file_content = "hello world"
    my_words = my_file_content.split()
except FileNotFoundError:
    print("My error: file not found")
else:
    print(f"My words: {my_words}")

# My try-except-finally (5)
try:
    my_nums = [1, 2, 3]
    my_item = my_nums[5]
except IndexError:
    print("My error: index out of range")
