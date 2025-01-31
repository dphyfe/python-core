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
print(f"My is subset: {my_small.issubset(my_large)}")
print(f"My is superset: {my_large.issuperset(my_small)}")

# My disjoint check (10)
my_a = {1, 2, 3}
my_b = {4, 5, 6}
print(f"My disjoint: {my_a.isdisjoint(my_b)}")

# My add and remove (11)
my_s = {1, 2, 3}
my_s.add(4)
my_s.remove(2)
print(f"My modified: {my_s}")

# My discard (12)
my_set = {1, 2, 3}
my_set.discard(2)
my_set.discard(10)
print(f"My after discard: {my_set}")

# My pop (13)
my_s = {1, 2, 3}
my_item = my_s.pop()
print(f"My popped: {my_item}")

# My clear (14)
my_set = {1, 2, 3}
my_set.clear()
print(f"My cleared: {my_set}")

# My copy (15)
my_original = {1, 2, 3}
my_copy = my_original.copy()
my_copy.add(4)
print(f"My original: {my_original}")
print(f"My copy: {my_copy}")

# Progress: part 2/2
