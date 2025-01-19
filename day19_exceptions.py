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
finally:
    print("My cleanup: always runs")

# My finally for resource cleanup (6)
try:
    my_f = open("my_temp_test.txt", "w")
    my_f.write("test content")
except IOError:
    print("My error: file operation failed")
finally:
    if 'my_f' in locals():
        my_f.close()
    print("My cleanup: file closed")

# My raising exceptions (7)
def my_validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True

try:
    my_validate_age(-5)
except ValueError as e:
    print(f"My error: {e}")

# My custom exception (8)
class MyCustomError(Exception):
    pass

def my_check_score(score):
    if score > 100:
        raise MyCustomError("Score cannot exceed 100")
    return True

try:
    my_check_score(150)
except MyCustomError as e:
    print(f"My custom error: {e}")

# My catching base exceptions (9)
try:
    my_risky = None
    my_result = my_risky.upper()
except AttributeError as e:
    print(f"My error: {e}")

# My bare except (catch all) (10)
try:
    my_x = 10 / 0
except:
    print("My error: something went wrong")

# My exception as variable (11)
try:
    my_list = [1, 2, 3]
    my_value = my_list[99]
except IndexError as my_error:
    print(f"My error details: {my_error}")
    print(f"My error type: {type(my_error)}")

# My assertion (12)
my_age = 30

# Progress: part 2/3
