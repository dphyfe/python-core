# Day 10: basic error handling for my practice

# My list for testing
my_numbers = [1, 2, 3]

# My first try/except with bad index (1)
try:
    print(my_numbers[5])
except IndexError:
    print("I tried to access index 5 but my list only has 3 items.")

# Another index error I'm catching
try:
    item = my_numbers[10]
except IndexError:
    print("I tried index 10 and got an error, which I expected.")

# Convert text to number safely for my practice (2)
my_text = "not_a_number"
try:
    my_value = int(my_text)
    print("I converted:", my_value)
except ValueError:
    print("I could not convert", my_text, "to int.")

# Another value error I'm handling
my_bad_input = "hello"
try:
    my_num = int(my_bad_input)
except ValueError:
    print("I can't turn 'hello' into a number.")

# My division by zero practice (3)
try:
    my_result = 10 / 0
    print(my_result)
except ZeroDivisionError:
    print("I cannot divide by zero.")

# Another division by zero
try:
    my_calc = 100 / 0
except ZeroDivisionError:
    print("I tried dividing 100 by zero and it failed as expected.")

# My dictionary key error (4)
my_pet = {"name": "Scout", "type": "dog"}
try:
    my_color = my_pet["color"]
    print(my_color)
except KeyError:
    print("I tried to get color but it's not in my dict.")

# Another key error for my practice
my_info = {"city": "Asheville"}
try:
    my_state = my_info["state"]
except KeyError:
    print("I don't have a state key in my info dict.")

# My file not found error (5)
try:
    with open("does_not_exist.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("I tried to open a file that doesn't exist.")

# Another file not found for my practice
try:
    with open("missing_file.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("I also tried missing_file.txt and it's not there.")

# My type error when mixing types (6)
try:
    my_mix = "age: " + 30
    print(my_mix)
except TypeError:
    print("I cannot add a string and a number together.")

# Another type error I'm catching
try:
    my_bad = "count: " + 5
except TypeError:
    print("I got a type error mixing string and int.")

# Using else with my try/except (7)
try:
    my_division = 10 / 2
except ZeroDivisionError:
    print("I shouldn't see this.")
else:
    print("My division worked:", my_division)

# Another else example for my learning
try:
    my_calc2 = 20 / 4
except ZeroDivisionError:
    print("Error occurred")
else:
    print("My calc2 succeeded:", my_calc2)

# Using a finally block for my cleanup (8)
try:
    print("I'm dividing numbers...")
    my_result2 = 10 / 2
    print("My result:", my_result2)
finally:
    print("I finished my division attempt.")

# Another finally for my practice
try:
    my_test = 15 / 3
    print("My test result:", my_test)
finally:
    print("I always run this finally block.")

# My multiple exception types
try:
    my_numbers[10]
except IndexError:
    print("I caught an index error.")
except ValueError:
    print("I caught a value error.")

# Catching multiple errors in one block
try:
    my_val = int("bad")
except (ValueError, TypeError):
    print("I caught either ValueError or TypeError.")

# Clean up with my try/finally (9)
my_file = None
try:
    my_file = open("day10_temp.txt", "w", encoding="utf-8")
    my_file.write("My temporary note for error handling demo.")
    print("I wrote my temp file.")
finally:
    if my_file:
        my_file.close()
        print("I closed my temp file.")

# Another file cleanup example
my_log = None
try:
    my_log = open("day10_log.txt", "w", encoding="utf-8")
    my_log.write("My log entry\n")
    print("I wrote to my log.")
finally:
    if my_log:
        my_log.close()
        print("I closed my log file.")

# My nested try/except practice
try:
    try:
        my_inner = 10 / 0
    except ZeroDivisionError:
        print("I caught the error in my inner try.")
        raise
except ZeroDivisionError:
    print("I caught it again in my outer try.")

# Catching generic exception for my learning
try:
    result = 1 / 0
except Exception as e:
    print("I caught a generic exception:", type(e).__name__)

# My assertion error practice
try:
    assert 1 == 2, "My assertion failed"
except AssertionError as e:
    print("I got an assertion error:", e)

# Practicing with name error
try:
    print(undefined_variable)
except NameError:
    print("I tried to use a variable that doesn't exist.")

# Progress: part 2/2
