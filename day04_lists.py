# Day 04: first lists (no loops yet)

# My mountain list for Western NC hikes
mountains = ["Blue Ridge", "Smoky", "Pisgah"]
foods = ["tacos", "ramen", "pizza", "bbq"]

print("My mountains:", mountains)
print("My favorite foods:", foods)

# Accessing items by my index (1-2)
first_mountain = mountains[0]
print("My first mountain:", first_mountain)
last_mountain = mountains[-1]
print("My last mountain:", last_mountain)

# Getting my second item
second_mountain = mountains[1]
print("My second mountain:", second_mountain)

# Slicing my list to get first two (3)
print("My first two mountains:", mountains[0:2])

# Slicing to get last two items
print("My last two mountains:", mountains[-2:])

# Changing an item in my food list (4)
foods[1] = "noodles"
print("I changed ramen to noodles:", foods)

# Changing my last food item
foods[-1] = "pulled pork"
print("I updated my last food:", foods)

# Adding items to my lists (5-6)
foods.append("ice cream")
print("I added dessert:", foods)

foods.append("coffee")
print("I added coffee too:", foods)

# Inserting items at specific positions in my list
foods.insert(2, "salad")
print("I inserted salad at position 2:", foods)

foods.insert(0, "breakfast burrito")
print("I put breakfast first:", foods)

# Extending my food list with more items (7)
foods.extend(["dumplings", "hotpot"])
print("I extended my foods:", foods)

# Adding more mountains to my list
mountains.append("Craggy")
print("I added Craggy to my mountains:", mountains)

mountains.append("Grandfather")
print("I added Grandfather Mountain:", mountains)

# Removing items from my lists (8-9)
removed = foods.pop(0)
print("I removed the first food:", removed)
print("My foods now:", foods)

removed_last = foods.pop()
print("I removed the last food:", removed_last)
print("My updated foods:", foods)

# Removing by value instead of index
if "pizza" in foods:
    foods.remove("pizza")
    print("I removed pizza:", foods)

# Checking if items are in my lists (10-11)
print("Do I have tacos?", "tacos" in foods)
print("Do I have sushi?", "sushi" in foods)
print("Is Blue Ridge in my mountains?", "Blue Ridge" in mountains)

# Getting lengths of my lists
print("My total mountains:", len(mountains))
print("My total foods:", len(foods))

# Creating more lists for my interests
activities = ["hiking", "coding", "reading"]
print("My activities:", activities)

dogs = ["Scout", "Luna"]
print("My dogs' names:", dogs)

# Combining lists together for my reference
all_interests = activities + dogs
print("My activities and dogs combined:", all_interests)

# Repeating my list (just practicing)
short_list = ["yes"]
repeated = short_list * 3
print("My repeated list:", repeated)

# Counting occurrences in my list
foods.append("tacos")
print("How many tacos in my list?", foods.count("tacos"))

# Finding index of an item in my list
if "noodles" in foods:
    noodle_index = foods.index("noodles")
    print("Noodles are at index:", noodle_index)

# Reversing my mountain list
mountains.reverse()
print("My reversed mountains:", mountains)

# Sorting my foods alphabetically
foods.sort()
print("My sorted foods:", foods)

# Making a copy of my list to keep original
foods_backup = foods.copy()
print("My backup foods:", foods_backup)

# Clearing a list when I'm done
temp_list = [1, 2, 3]
print("My temp list before clear:", temp_list)
temp_list.clear()
print("My temp list after clear:", temp_list)
