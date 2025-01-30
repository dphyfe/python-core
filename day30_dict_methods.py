# Day 30: dictionary methods for my practice

# My get method (1)
my_dict = {"name": "David", "age": 30}
my_name = my_dict.get("name")
my_missing = my_dict.get("city")
print(f"My name: {my_name}")
print(f"My missing: {my_missing}")

# My get with default (2)
my_city = my_dict.get("city", "Asheville")
print(f"My city default: {my_city}")

# My setdefault (3)
my_dict = {"name": "David"}
my_dict.setdefault("age", 30)
my_dict.setdefault("name", "Taylor")
print(f"My dict: {my_dict}")

# My keys method (4)
my_dict = {"a": 1, "b": 2, "c": 3}
my_keys = my_dict.keys()
print(f"My keys: {list(my_keys)}")

# My values method (5)
my_values = my_dict.values()
print(f"My values: {list(my_values)}")

# My items method (6)
my_items = my_dict.items()
print(f"My items: {list(my_items)}")

# My pop method (7)
my_dict = {"a": 1, "b": 2, "c": 3}
my_val = my_dict.pop("b")
print(f"My popped: {my_val}")
print(f"My dict after pop: {my_dict}")

# My pop with default (8)
my_removed = my_dict.pop("z", "not found")
print(f"My pop default: {my_removed}")

# My update method (9)
my_dict = {"a": 1, "b": 2}
my_dict.update({"b": 20, "c": 3})
print(f"My updated: {my_dict}")

# My clear method (10)
my_dict = {"a": 1, "b": 2}
my_dict.clear()
print(f"My cleared: {my_dict}")

# My copy method (11)
my_original = {"a": 1, "b": 2}
my_copy = my_original.copy()
my_copy["a"] = 99
print(f"My original: {my_original}")
print(f"My copy: {my_copy}")

# My popitem method (12)
my_dict = {"a": 1, "b": 2, "c": 3}
my_last = my_dict.popitem()
print(f"My popped item: {my_last}")

# My fromkeys (13)
my_keys = ["a", "b", "c"]
my_new_dict = dict.fromkeys(my_keys, 0)
print(f"My fromkeys: {my_new_dict}")

# My in operator (14)
my_dict = {"name": "David", "age": 30}
print(f"My 'name' in dict: {'name' in my_dict}")
print(f"My 'city' in dict: {'city' in my_dict}")

# My iteration (15)
my_dict = {"a": 1, "b": 2}
for my_key, my_val in my_dict.items():
    print(f"My {my_key}: {my_val}")
