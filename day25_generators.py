# Day 25: generators for my practice

# My simple generator (1)
def my_count_up(max):
    my_current = 0
    while my_current < max:
        yield my_current
        my_current += 1

for my_num in my_count_up(5):
    print(f"My count: {my_num}")

# My generator vs list (2)
def my_generate_squares(n):
    for i in range(n):
        yield i * i

my_squares = my_generate_squares(5)
print(f"My generator: {my_squares}")
my_first = next(my_squares)
print(f"My first square: {my_first}")

# My generator with list comprehension (3)
my_list_squares = [i * i for i in range(5)]
print(f"My list: {my_list_squares}")

my_gen_squares = (i * i for i in range(5))
my_first_gen = next(my_gen_squares)
print(f"My first from gen: {my_first_gen}")

# My fibonacci generator (4)
def my_fibonacci(max):
    my_a, my_b = 0, 1
    while my_a < max:
        yield my_a
        my_a, my_b = my_b, my_a + my_b

for my_fib in my_fibonacci(20):
    print(f"My fib: {my_fib}")

# My generator with multiple yields (5)
def my_colors():
    yield "red"
    yield "green"
    yield "blue"

for my_color in my_colors():
    print(f"My color: {my_color}")

# My generator with condition (6)
def my_even_numbers(max):
    for i in range(max):
        if i % 2 == 0:
            yield i

my_evens = list(my_even_numbers(10))
print(f"My evens: {my_evens}")

# My generator with argument (7)
def my_repeat_string(text, times):
    for _ in range(times):
        yield text

for my_text in my_repeat_string("hello", 3):
    print(f"My text: {my_text}")

# My generator for file processing (8)
def my_read_large_file(filename, chunk_size=1024):
    with open(filename, "r") as f:
        while True:
            my_chunk = f.read(chunk_size)
            if not my_chunk:
                break
            yield my_chunk

# Create temp file
with open("my_large_file.txt", "w") as f:
    f.write("A" * 5000)

for my_chunk in my_read_large_file("my_large_file.txt", 100):
    print(f"My chunk size: {len(my_chunk)}")

# My generator composition (9)
def my_integers():
    my_i = 0
    while True:
        yield my_i
        my_i += 1

def my_take(n, iterable):
    for _ in range(n):
        yield next(iterable)

for my_val in my_take(3, my_integers()):
    print(f"My value: {my_val}")

# My generator with filter (10)
def my_filter_positive(numbers):
    for num in numbers:
        if num > 0:
            yield num

my_nums = [-1, 2, -3, 4, -5, 6]
for my_num in my_filter_positive(my_nums):
    print(f"My positive: {my_num}")

# My send to generator (11)
def my_echo_generator():
    while True:
        my_received = yield
        if my_received:
            print(f"My received: {my_received}")

my_gen = my_echo_generator()
next(my_gen)
my_gen.send("hello")

# My generator expression (12)
my_squares_exp = (x**2 for x in range(5))
print(f"My first square: {next(my_squares_exp)}")

# My generator with finally (13)
def my_cleanup_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("My cleanup")

for my_val in my_cleanup_gen():
    print(f"My val: {my_val}")

# Cleanup
import os
if os.path.exists("my_large_file.txt"):
    os.remove("my_large_file.txt")

# My generator infinite sequence (14)
def my_infinite_counter():
    my_count = 0
    while True:
        yield my_count
        my_count += 1

my_counter = my_infinite_counter()
print(f"My first: {next(my_counter)}")
print(f"My second: {next(my_counter)}")
print(f"My third: {next(my_counter)}")

# My generator range alternative (15)
def my_my_range(start, end, step=1):
    my_current = start
    while my_current < end:
        yield my_current
        my_current += step

for my_i in my_my_range(0, 10, 2):
    print(f"My range value: {my_i}")
