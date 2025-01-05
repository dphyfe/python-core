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
