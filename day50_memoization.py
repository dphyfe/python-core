# Day 50: memoization for my practice

def my_fib_slow(n):
    if n <= 1:
        return n
    return my_fib_slow(n-1) + my_fib_slow(n-2)

print(f"My slow fib(10): {my_fib_slow(10)}")

my_cache = {}

def my_fib_cached(n):
    if n in my_cache:
        return my_cache[n]
    if n <= 1:
        return n
    result = my_fib_cached(n-1) + my_fib_cached(n-2)
    my_cache[n] = result
    return result

print(f"My cached fib(30): {my_fib_cached(30)}")

from functools import lru_cache

@lru_cache(maxsize=None)
def my_fib_lru(n):
    if n <= 1:
        return n
    return my_fib_lru(n-1) + my_fib_lru(n-2)

print(f"My lru fib(30): {my_fib_lru(30)}")
print(f"My cache info: {my_fib_lru.cache_info()}")

@lru_cache(maxsize=128)
def my_factorial(n):
    if n <= 1:
        return 1
    return n * my_factorial(n-1)

print(f"My factorial(10): {my_factorial(10)}")
print(f"My cache info: {my_factorial.cache_info()}")

my_factorial.cache_clear()
print(f"My cache cleared: {my_factorial.cache_info()}")

def my_memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@my_memoize
def my_sum_to(n):
    if n <= 0:
        return 0
    return n + my_sum_to(n-1)

print(f"My sum_to(100): {my_sum_to(100)}")
