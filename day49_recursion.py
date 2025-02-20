# Day 49: recursion basics for my practice

def my_factorial(n):
    if n <= 1:
        return 1
    return n * my_factorial(n - 1)

print(f"My 5! = {my_factorial(5)}")

def my_fibonacci(n):
    if n <= 1:
        return n
    return my_fibonacci(n-1) + my_fibonacci(n-2)

print(f"My fib(6) = {my_fibonacci(6)}")

def my_sum_list(items):
    if not items:
        return 0
    return items[0] + my_sum_list(items[1:])

my_nums = [1, 2, 3, 4, 5]
print(f"My sum: {my_sum_list(my_nums)}")

def my_countdown(n):
    if n <= 0:
        print("My blastoff!")
        return
    print(f"My count: {n}")
    my_countdown(n - 1)

my_countdown(5)

def my_power(base, exp):
    if exp == 0:
        return 1
    return base * my_power(base, exp - 1)

print(f"My 2^4 = {my_power(2, 4)}")

def my_reverse_string(s):
    if len(s) <= 1:
        return s
    return my_reverse_string(s[1:]) + s[0]

print(f"My reversed: {my_reverse_string('hello')}")

def my_flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(my_flatten(item))
        else:
            result.append(item)
    return result

my_nested = [1, [2, 3], [4, [5, 6]]]
print(f"My flattened: {my_flatten(my_nested)}")

# Progress: part 2/2
