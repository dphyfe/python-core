# Day 33: tuple unpacking and *args for my practice

# My basic unpacking (1)
my_tuple = (1, 2, 3)
my_a, my_b, my_c = my_tuple
print(f"My a: {my_a}, b: {my_b}, c: {my_c}")

# My unpacking in loop (2)
my_pairs = [(1, "a"), (2, "b"), (3, "c")]
for my_num, my_letter in my_pairs:
    print(f"My {my_num}: {my_letter}")

# My unpacking with * (3)
my_data = (1, 2, 3, 4, 5)
my_first, *my_rest = my_data
print(f"My first: {my_first}")
print(f"My rest: {my_rest}")

# My unpacking with * middle (4)
my_first, *my_middle, my_last = my_data
print(f"My first: {my_first}, last: {my_last}")
print(f"My middle: {my_middle}")

# My unpacking underscore (5)
my_x, _, my_z = (1, 2, 3)
print(f"My x: {my_x}, z: {my_z}")

# My unpacking lists (6)
my_list = [10, 20, 30]
my_a, my_b, my_c = my_list
print(f"My list unpacked: {my_a}, {my_b}, {my_c}")

# My *args in functions (7)
def my_sum(*args):
    my_total = 0
    for num in args:
        my_total += num
    return my_total

print(f"My sum: {my_sum(1, 2, 3, 4, 5)}")

# My *args with regular args (8)
def my_greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

my_greet("Hello", "David", "Taylor", "Alex")

# My unpacking with ** (9)
def my_person_info(name, age, city):
    print(f"My name: {name}, age: {age}, city: {city}")

my_dict = {"name": "David", "age": 30, "city": "Asheville"}
my_person_info(**my_dict)

# My **kwargs (10)
def my_show_kwargs(**kwargs):
    for my_key, my_val in kwargs.items():
        print(f"My {my_key}: {my_val}")

my_show_kwargs(name="David", age=30, city="Asheville")

# My packing with * (11)
my_items = [1, 2, 3]
my_packed = [0, *my_items, 4]
print(f"My packed: {my_packed}")

# My unpacking in assignment (12)
my_a, my_b = 1, 2
print(f"My a: {my_a}, b: {my_b}")

my_a, my_b = my_b, my_a
print(f"My swapped: a: {my_a}, b: {my_b}")

# My nested unpacking (13)
my_data = (1, (2, 3), 4)
my_a, (my_b, my_c), my_d = my_data
print(f"My nested: {my_a}, {my_b}, {my_c}, {my_d}")

# My unpacking empty (14)
my_first, *my_rest = [1]
print(f"My first: {my_first}, rest: {my_rest}")

# My unpacking function call (15)
def my_max_args(a, b, c):
    return max(a, b, c)

my_values = [10, 5, 20]
my_result = my_max_args(*my_values)
print(f"My max: {my_result}")
