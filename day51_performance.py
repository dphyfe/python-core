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
