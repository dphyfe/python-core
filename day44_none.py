# Day 44: working with None for my practice

my_var = None
print(f"My var: {my_var}")
print(f"My type: {type(my_var)}")

if my_var is None:
    print("My var is None")

my_list = [1, None, 3, None, 5]
my_clean = [x for x in my_list if x is not None]
print(f"My cleaned: {my_clean}")

def my_maybe_return(flag):
    if flag:
        return "value"
    return None

my_result = my_maybe_return(False)
print(f"My result: {my_result}")

my_dict = {"a": 1, "b": None, "c": 3}

# Progress: part 2/4
