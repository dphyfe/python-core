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
@my_timer
def my_concat_strings():
    result = ""
    for _ in range(10000):
        result += my_string
    return result

@my_timer
def my_join_strings():
    return "".join([my_string for _ in range(10000)])

my_concat_strings()
my_join_strings()

my_data = [{"name": "David", "age": 30} for _ in range(100)]

@my_timer
def my_filter_dict_comp():
    return [d for d in my_data if d["age"] > 25]

@my_timer
def my_filter_builtin():
    return list(filter(lambda d: d["age"] > 25, my_data))

my_filter_dict_comp()
my_filter_builtin()

# Progress: part 6/6
