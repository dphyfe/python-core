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
