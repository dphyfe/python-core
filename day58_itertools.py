# Day 58: itertools for my practice

from itertools import count, cycle, repeat, chain, combinations, permutations

my_counter = count(10, 2)
for _ in range(5):
    print(f"My count: {next(my_counter)}")

my_cycler = cycle([1, 2, 3])
for _, val in zip(range(7), my_cycler):
    print(f"My cycle: {val}")

my_repeater = repeat("hello", 3)
for val in my_repeater:
    print(f"My repeat: {val}")

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_chained = chain(my_list1, my_list2)
print(f"My chained: {list(my_chained)}")

my_items = [1, 2, 3]
my_combos = combinations(my_items, 2)
print(f"My combinations: {list(my_combos)}")

my_perms = permutations([1, 2, 3], 2)
print(f"My permutations: {list(my_perms)}")

from itertools import product, islice

my_prod = product([1, 2], ['a', 'b'])
print(f"My product: {list(my_prod)}")

my_infinite = count()
my_limited = islice(my_infinite, 5)
print(f"My islice: {list(my_limited)}")

from itertools import groupby

my_data = [1, 1, 2, 2, 2, 3, 1, 1]
my_grouped = [(k, list(g)) for k, g in groupby(my_data)]
print(f"My grouped: {my_grouped}")

from itertools import accumulate
my_nums = [1, 2, 3, 4, 5]
my_accumulated = accumulate(my_nums)
print(f"My accumulated: {list(my_accumulated)}")

from itertools import filterfalse
my_filtered = filterfalse(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(f"My filterfalse: {list(my_filtered)}")

from itertools import takewhile
my_taken = takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 3, 2])
print(f"My takewhile: {list(my_taken)}")

# Progress: part 2/2
