# Day 46: assertions for my practice

my_age = 30
assert my_age > 0, "Age must be positive"
print("My age assertion passed")

my_nums = [1, 2, 3]
assert len(my_nums) == 3
print("My length assertion passed")

def my_divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

my_result = my_divide(10, 2)
print(f"My division: {my_result}")

try:
    my_divide(10, 0)
except AssertionError as e:
    print(f"My assertion error: {e}")

my_dict = {"name": "David"}
assert "name" in my_dict
print("My key assertion passed")

my_value = 42
assert isinstance(my_value, int)
