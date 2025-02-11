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
