# Day 06: tiny functions for my practice

# My simple greeter function

def greet(name):
    message = "Hello, " + name + "!"
    return message


# My function to add two numbers

def add_numbers(a, b):
    result = a + b
    return result


# My function to multiply two numbers

def multiply(a, b):
    return a * b


# My function to subtract

def subtract(a, b):
    return a - b


# My function to get the first item from a list

def list_first(items):
    if len(items) == 0:
        return "No items"
    return items[0]


# My function to get the last item

def list_last(items):
    if len(items) == 0:
        return "No items"
    return items[-1]


# My function to describe a city

def describe_city(city, state):
    return city + ", " + state


# My function to describe my location

def my_location(city):
    return "I live in " + city


# My function to repeat a phrase

def repeat_phrase(phrase, times):
    result = []
    for _ in range(times):
        result.append(phrase)
    return " ".join(result)


# My function to check if a number is even

def is_even(number):
    return number % 2 == 0


# My function to check if a number is odd

def is_odd(number):
    return number % 2 != 0


# My function to count items in a list

def count_items(items):
    count = 0
    for _ in items:
        count = count + 1
    return count


# My function to sum a list of numbers

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


# My function to average a list of numbers

def average_numbers(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)


# My function to format a pet description

def format_pet(name, animal_type):
    return "Pet: " + name + " the " + animal_type


# My function to build a full name

def full_name(first, last):
    return first + " " + last


# My function to convert Fahrenheit to Celsius

def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# My function to convert Celsius to Fahrenheit

def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# My function to square a number

def square(number):
    return number * number


# My function to check if a string is long

def is_long_word(word):
    return len(word) > 7


# My function to make a greeting for hiking

def hiking_greeting(name, mountain):
    return name + " is hiking " + mountain


# My function to double a number

def double(number):
    return number * 2


# Now I call all my functions
print(greet("David"))
print(greet("Taylor"))

sum_value = add_numbers(3, 4)
print("My sum:", sum_value)
print("My multiplication:", multiply(5, 6))
print("My subtraction:", subtract(10, 3))

mountains = ["Blue Ridge", "Pisgah", "Craggy"]
print("My first mountain:", list_first(mountains))
print("My last mountain:", list_last(mountains))
print("First from my empty list:", list_first([]))

print("My city and state:", describe_city("Asheville", "NC"))
print("My location:", my_location("Asheville"))
