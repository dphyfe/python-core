# Day 31: set operations for my practice

# My set creation (1)
my_set = {1, 2, 3, 4, 5}
print(f"My set: {my_set}")

# My set from list (2)
my_list = [1, 2, 2, 3, 3, 3]
my_unique = set(my_list)
print(f"My unique: {my_unique}")

# My union (3)
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_union = my_set1 | my_set2
print(f"My union: {my_union}")

# My intersection (4)
my_inter = my_set1 & my_set2
print(f"My intersection: {my_inter}")

# My difference (5)
my_diff = my_set1 - my_set2
print(f"My difference: {my_diff}")

# My symmetric difference (6)
my_sym = my_set1 ^ my_set2
print(f"My symmetric difference: {my_sym}")

# My set methods - union (7)
my_u = my_set1.union(my_set2)
print(f"My union method: {my_u}")

# My intersection update (8)
my_s1 = {1, 2, 3}
my_s2 = {2, 3, 4}
my_s1.intersection_update(my_s2)
print(f"My after intersection_update: {my_s1}")

# My subset check (9)
my_small = {1, 2}
my_large = {1, 2, 3, 4}
