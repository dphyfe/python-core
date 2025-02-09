# Day 40: copy vs reference for my practice

# My list reference (1)
my_list1 = [1, 2, 3]
my_list2 = my_list1
my_list2[0] = 99
print(f"My list1: {my_list1}")
print(f"My list2: {my_list2}")

# My list copy (2)
my_original = [1, 2, 3]
my_copy = my_original.copy()
my_copy[0] = 99
print(f"My original: {my_original}")
print(f"My copy: {my_copy}")

# My slice copy (3)
my_orig = [1, 2, 3]
my_sliced = my_orig[:]
my_sliced[0] = 99
print(f"My orig: {my_orig}")
print(f"My sliced: {my_sliced}")

# My dict reference (4)
my_dict1 = {"a": 1}
my_dict2 = my_dict1
my_dict2["a"] = 99
print(f"My dict1: {my_dict1}")

# My dict copy (5)
my_d1 = {"a": 1, "b": 2}
my_d2 = my_d1.copy()
my_d2["a"] = 99
print(f"My d1: {my_d1}")
print(f"My d2: {my_d2}")

# My nested list shallow copy (6)
my_nested = [[1, 2], [3, 4]]
my_shallow = my_nested.copy()
my_shallow[0][0] = 99
print(f"My nested: {my_nested}")
print(f"My shallow: {my_shallow}")

# My deepcopy (7)
import copy
my_deep_orig = [[1, 2], [3, 4]]
my_deep_copy = copy.deepcopy(my_deep_orig)
my_deep_copy[0][0] = 99
print(f"My deep orig: {my_deep_orig}")
print(f"My deep copy: {my_deep_copy}")

# My immutable types (8)
my_int1 = 5
my_int2 = my_int1
my_int2 = 10
print(f"My int1: {my_int1}")
print(f"My int2: {my_int2}")

# My string immutable (9)
my_str1 = "hello"
my_str2 = my_str1
my_str2 = "world"
print(f"My str1: {my_str1}")
print(f"My str2: {my_str2}")

# My tuple reference (10)
my_t1 = (1, 2, 3)
my_t2 = my_t1
print(f"My same tuple: {my_t1 is my_t2}")

# My is vs == (11)
my_a = [1, 2, 3]
my_b = [1, 2, 3]
print(f"My == : {my_a == my_b}")
print(f"My is: {my_a is my_b}")

# My list constructor copy (12)
my_src = [1, 2, 3]
my_new = list(my_src)
my_new[0] = 99
print(f"My src: {my_src}")
print(f"My new: {my_new}")

# My dict constructor copy (13)
my_d_src = {"a": 1}
my_d_new = dict(my_d_src)
my_d_new["a"] = 99
print(f"My d src: {my_d_src}")
print(f"My d new: {my_d_new}")

# My function parameter (14)
def my_modify(lst):
    lst.append(4)

my_input = [1, 2, 3]
my_modify(my_input)
print(f"My modified input: {my_input}")

# My id function (15)
my_x = [1, 2]
my_y = my_x
print(f"My same id: {id(my_x) == id(my_y)}")
