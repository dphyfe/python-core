# Day 14: more functions with args and kwargs for my practice

# My function with default argument (1)
def my_greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(my_greet("David"))
print(my_greet("Taylor", "Hi"))
print(my_greet("Scout", "Woof"))

# Another default example (2)
def my_city_info(city, state="NC"):
    return f"{city}, {state}"

print(my_city_info("Asheville"))
print(my_city_info("Durham"))
print(my_city_info("Atlanta", "GA"))

# My function with multiple defaults (3)
def my_profile(name, age=30, city="Asheville"):
    return f"{name}, {age} years old, from {city}"

print(my_profile("David"))
print(my_profile("Taylor", 28))
print(my_profile("Alex", 25, "Durham"))

# My function with *args (variable positional) (4)
def my_sum(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print("My sum of 1,2,3:", my_sum(1, 2, 3))
print("My sum of 5,10,15,20:", my_sum(5, 10, 15, 20))
print("My sum of single number:", my_sum(42))

# Another *args example (5)
def my_list_mountains(*mountains):
    print("My mountains:")
    for mountain in mountains:
        print("-", mountain)

my_list_mountains("Blue Ridge", "Smoky", "Pisgah")
my_list_mountains("Craggy", "Grandfather")

# My function combining regular and *args (6)
def my_introduce(name, *hobbies):
    print(f"My name is {name}")
    print("My hobbies:")
    for hobby in hobbies:
        print("-", hobby)

my_introduce("David", "hiking", "coding", "reading")

# My function with **kwargs (variable keyword) (7)
def my_show_info(**info):
    print("My info:")
    for key, value in info.items():
        print(f"  {key}: {value}")

my_show_info(name="David", city="Asheville", age=30)
my_show_info(dog="Scout", age=3, breed="mixed")

# My function with all three: normal, *args, **kwargs (8)
def my_full_function(required, *args, **kwargs):
    print(f"My required: {required}")
    print(f"My args: {args}")
    print(f"My kwargs: {kwargs}")

my_full_function("first", "second", "third", name="David", city="Asheville")

# My function returning multiple values (tuple) (9)
def my_calculate(a, b):
    my_sum = a + b
    my_diff = a - b
    my_product = a * b
    return my_sum, my_diff, my_product

my_s, my_d, my_p = my_calculate(10, 5)
print(f"My results: sum={my_s}, diff={my_d}, product={my_p}")

# My lambda function (small anonymous) (10)
my_double = lambda x: x * 2
print("My doubled 5:", my_double(5))
print("My doubled 10:", my_double(10))

# Another lambda
my_square = lambda x: x * x
print("My squared 4:", my_square(4))

# My lambda with multiple args (11)
my_add = lambda a, b: a + b
print("My lambda sum:", my_add(3, 7))

# My map with lambda (12)
my_numbers = [1, 2, 3, 4, 5]
my_doubled = list(map(lambda x: x * 2, my_numbers))
print("My mapped doubled:", my_doubled)

# My filter with lambda (13)
my_evens = list(filter(lambda x: x % 2 == 0, my_numbers))
print("My filtered evens:", my_evens)

# My sorted with lambda key (14)
my_words = ["hiking", "dog", "Asheville", "run"]
my_sorted_by_length = sorted(my_words, key=lambda w: len(w))
print("My sorted by length:", my_sorted_by_length)
