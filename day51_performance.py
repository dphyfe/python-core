# Day 51: performance tips for my practice

import time

def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"My {func.__name__} took {end-start:.6f}s")
        return result
    return wrapper

@my_timer
def my_list_comp():
    return [x*2 for x in range(100000)]

@my_timer
def my_map_version():
    return list(map(lambda x: x*2, range(100000)))

my_list_comp()
my_map_version()

my_nums = list(range(1000))

@my_timer
def my_check_membership_list():
    return 999 in my_nums

@my_timer
def my_check_membership_set():
    my_set = set(my_nums)
    return 999 in my_set

my_check_membership_list()
my_check_membership_set()

my_string = "hello "

# Progress: part 3/6
