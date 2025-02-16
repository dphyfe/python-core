# Day 45: boolean logic for my practice

my_true = True
my_false = False
print(f"My and: {my_true and my_false}")
print(f"My or: {my_true or my_false}")
print(f"My not: {not my_true}")

my_a = 5
my_b = 10
print(f"My comparison: {my_a < my_b and my_b > 0}")

my_values = [1, 2, 3, 4, 5]
my_result = all(x > 0 for x in my_values) and any(x % 2 == 0 for x in my_values)
print(f"My complex: {my_result}")

my_truthy = [1, "hello", [1], {"a": 1}]
my_falsy = [0, "", [], {}, None, False]
