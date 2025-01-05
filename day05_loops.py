# Day 05: first loops over lists

# My mountain and food lists
mountains = ["Blue Ridge", "Smoky", "Pisgah", "Craggy"]
foods = ["tacos", "noodles", "pizza"]

print("My mountains in Western NC:")
for mountain in mountains:
    print("-", mountain)

print("\nMy favorite foods:")
for food in foods:
    print("-", food)

# Counting items with my loop (1)
count = 0
for food in foods:
    count = count + 1
print("I counted", count, "foods")

# Counting my mountains
mountain_count = 0
for mountain in mountains:
    mountain_count = mountain_count + 1
print("I have", mountain_count, "mountains in my list")

# My range loop to print numbers (2)
print("My first five numbers:")
for number in range(1, 6):
    print(number)

# Another range loop I'm practicing
print("My numbers from 0 to 4:")
for i in range(5):
    print(i)

# My range with a step
print("My even numbers up to 10:")
for num in range(0, 11, 2):
    print(num)

# Loop to build my uppercase list (3)
upper_mountains = []
for mountain in mountains:
    upper_mountains.append(mountain.upper())
print("My uppercase mountains:", upper_mountains)

# Loop to build my lowercase foods
lower_foods = []
for food in foods:
    lower_foods.append(food.lower())
print("My lowercase foods:", lower_foods)

# My while loop countdown (4)
countdown = 3
print("My countdown:")
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("My countdown is done")

# Another while loop I'm trying
counter = 0
print("My counter going up:")
while counter < 3:
    print("Counter at:", counter)
    counter = counter + 1

# Loop with continue to skip items (5)
print("My foods without pizza:")
for food in foods:
    if food == "pizza":
        continue
    print(food)

# Another continue example for my practice
print("My mountains except Smoky:")
for mountain in mountains:
    if mountain == "Smoky":
        continue
    print(mountain)

# My loop with break (6)
print("I'm stopping when I see Smoky:")
for mountain in mountains:
    print(mountain)
    if mountain == "Smoky":
        break

# Another break example in my loop
print("I stop at pizza:")
for food in foods:
    if food == "pizza":
        break
    print(food)

# Sum numbers with my loop (7)
numbers = [1, 2, 3, 4]
total = 0
for number in numbers:
    total = total + number
print("My total sum:", total)

# Summing more numbers for my practice
my_values = [10, 20, 30]
my_sum = 0
for value in my_values:
    my_sum = my_sum + value
print("My sum of values:", my_sum)

# Building a list of doubled numbers
doubled = []
for number in numbers:
    doubled.append(number * 2)
print("My doubled numbers:", doubled)

# Enumerate in my loop (8)
print("My indexed mountains:")
for index, mountain in enumerate(mountains):
    print("Position", index, "has", mountain)

# Enumerate with my foods
print("My indexed foods:")
for i, food in enumerate(foods):
    print(i, ":", food)

# Enumerate starting from 1 for my list
print("My mountains starting count at 1:")
for position, mountain in enumerate(mountains, start=1):
    print(position, mountain)

# Nested loop for my combinations (9)
print("My mountain + food pairs:")
for mountain in mountains:
    for food in foods:
        print(mountain, "with", food)

# Another nested loop example I'm practicing
colors = ["blue", "green"]
sizes = ["small", "large"]
print("My color and size combos:")
for color in colors:
    for size in sizes:
        print(color, size)

# Loop to collect only long names
long_mountains = []
for mountain in mountains:
    if len(mountain) > 5:
        long_mountains.append(mountain)
print("My long mountain names:", long_mountains)

# Loop to check if any food starts with 't'
print("My foods starting with 't':")
for food in foods:
    if food.startswith("t"):
        print(food)

# Progress: part 3/3
