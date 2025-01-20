# Day 20: decorators and functional programming for my practice

# My simple decorator (1)
def my_simple_decorator(func):
    def my_wrapper(*args, **kwargs):
        print("My before function")
        result = func(*args, **kwargs)
        print("My after function")
        return result
    return my_wrapper

@my_simple_decorator
def my_greeting(name):
    return f"Hello, {name}!"

print(my_greeting("David"))

# My decorator with arguments (2)
def my_repeat_decorator(times):
    def my_actual_decorator(func):
        def my_wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Iteration {i+1}")
                result = func(*args, **kwargs)
            return result
        return my_wrapper
    return my_actual_decorator

@my_repeat_decorator(3)
def my_say_hello():
    print("Hello!")

my_say_hello()

# My timer decorator (3)
import time

def my_timer_decorator(func):
    def my_wrapper(*args, **kwargs):
        my_start = time.time()
        result = func(*args, **kwargs)
        my_end = time.time()
        my_elapsed = my_end - my_start
        print(f"My execution time: {my_elapsed:.4f} seconds")
        return result
    return my_wrapper

@my_timer_decorator
def my_slow_function():
    time.sleep(0.1)
    return "Done"

my_slow_function()

# My validation decorator (4)
def my_validate_positive(func):
    def my_wrapper(num):
        if num < 0:
            raise ValueError("Must be positive")
        return func(num)
    return my_wrapper

@my_validate_positive
def my_square(x):
    return x * x

print("My square of 5:", my_square(5))

try:
    my_square(-5)
except ValueError as e:
    print(f"My error: {e}")

# My functools.wraps (5)
from functools import wraps

def my_better_decorator(func):
    @wraps(func)
    def my_wrapper(*args, **kwargs):
        print("My wrapper")
        return func(*args, **kwargs)
    return my_wrapper

@my_better_decorator
def my_documented_func():
    """My docstring"""
    pass

print("My func name:", my_documented_func.__name__)
print("My func doc:", my_documented_func.__doc__)

# My stacking decorators (6)
def my_decorator_a(func):
    def my_wrapper(*args, **kwargs):
        print("A before")
        result = func(*args, **kwargs)
        print("A after")
        return result
    return my_wrapper

def my_decorator_b(func):
    def my_wrapper(*args, **kwargs):
        print("B before")
        result = func(*args, **kwargs)
        print("B after")
        return result
    return my_wrapper

@my_decorator_a
@my_decorator_b
def my_stacked():
    print("Inside function")

my_stacked()

# My function as first-class object (7)
def my_add(a, b):
    return a + b

def my_subtract(a, b):
    return a - b

my_operations = [my_add, my_subtract]
for op in my_operations:
    print(f"Result: {op(10, 5)}")

# My higher-order function (8)
def my_higher_order(func, data):
    return [func(x) for x in data]

my_numbers = [1, 2, 3, 4, 5]
my_doubled = my_higher_order(lambda x: x * 2, my_numbers)
print("My doubled:", my_doubled)

# My map function (9)
my_values = [1, 2, 3, 4, 5]
my_squared = list(map(lambda x: x ** 2, my_values))
print("My squared:", my_squared)

# My filter function (10)
my_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_evens = list(filter(lambda x: x % 2 == 0, my_items))
print("My evens:", my_evens)

# My reduce function (11)
from functools import reduce

my_numbers_list = [1, 2, 3, 4, 5]
my_product = reduce(lambda a, b: a * b, my_numbers_list)
print("My product:", my_product)

# My partial function (12)
from functools import partial

def my_power(base, exponent):
    return base ** exponent

my_square_func = partial(my_power, exponent=2)
print("My square of 5:", my_square_func(5))

my_cube_func = partial(my_power, exponent=3)
print("My cube of 3:", my_cube_func(3))

# My pure function (13)
def my_pure_add(a, b):
    return a + b

# Good - no side effects
my_result1 = my_pure_add(3, 5)
my_result2 = my_pure_add(3, 5)
print(f"My pure results always same: {my_result1 == my_result2}")

# My key function in sorted (14)
my_words_list = ["python", "cat", "dog", "elephant"]
my_sorted_by_length = sorted(my_words_list, key=len)
print("My sorted by length:", my_sorted_by_length)

my_sorted_by_char = sorted(my_words_list, key=lambda w: w[-1])
print("My sorted by last char:", my_sorted_by_char)
