# Day 42: closures for my practice

def my_outer(x):
    def my_inner(y):
        return x + y
    return my_inner

my_add5 = my_outer(5)
print(f"My result: {my_add5(3)}")

def my_multiplier(factor):
    def my_multiply(value):
        return value * factor
    return my_multiply

my_double = my_multiplier(2)
my_triple = my_multiplier(3)
print(f"My doubled: {my_double(10)}")
print(f"My tripled: {my_triple(10)}")

def my_counter():
    my_count = 0
    def my_increment():
        nonlocal my_count
        my_count += 1
        return my_count
    return my_increment

my_c1 = my_counter()
print(f"My count: {my_c1()}")
print(f"My count: {my_c1()}")

# Progress: part 3/3
