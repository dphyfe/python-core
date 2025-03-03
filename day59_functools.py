# Day 59: functools for my practice

from functools import reduce, partial, wraps

my_nums = [1, 2, 3, 4, 5]
my_sum = reduce(lambda x, y: x + y, my_nums)
print(f"My sum: {my_sum}")

my_product = reduce(lambda x, y: x * y, my_nums)
print(f"My product: {my_product}")

def my_multiply(x, y):
    return x * y

my_double = partial(my_multiply, 2)
print(f"My doubled: {my_double(5)}")

my_triple = partial(my_multiply, 3)
print(f"My tripled: {my_triple(5)}")

from functools import lru_cache

@lru_cache(maxsize=128)
def my_fib(n):
    if n <= 1:
        return n
    return my_fib(n-1) + my_fib(n-2)

print(f"My fib(30): {my_fib(30)}")
print(f"My cache info: {my_fib.cache_info()}")

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"My calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_greet(name):
    """My greeting function"""
    return f"Hello, {name}"

print(my_greet("David"))
print(f"My docstring: {my_greet.__doc__}")

from functools import total_ordering

@total_ordering
class MyNumber:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value

my_n1 = MyNumber(5)
my_n2 = MyNumber(10)
print(f"My less: {my_n1 < my_n2}")
print(f"My greater: {my_n1 > my_n2}")
print(f"My lte: {my_n1 <= my_n2}")

from functools import singledispatch

@singledispatch
def my_process(arg):
    print(f"My default: {arg}")

@my_process.register(int)
def _(arg):
    print(f"My int: {arg * 2}")

@my_process.register(str)
def _(arg):
    print(f"My string: {arg.upper()}")

my_process(5)
my_process("hello")
my_process([1, 2, 3])

# Progress: part 2/2
