# Day 13: tuples and sets for my practice

# My first tuple (1)
my_location = ("Asheville", "NC", 28801)
print("My location tuple:", my_location)

my_dog = ("Scout", 3, "mixed")
print("My dog tuple:", my_dog)

# Accessing my tuple items (2)
my_city = my_location[0]
my_state = my_location[1]
print("My city:", my_city)
print("My state:", my_state)

# My tuple unpacking (3)
city, state, zipcode = my_location
print(f"I unpacked: {city}, {state} {zipcode}")

name, age, breed = my_dog
print(f"My dog: {name}, age {age}, {breed}")

# My tuple concatenation (4)
my_first = (1, 2, 3)
my_second = (4, 5, 6)
my_combined = my_first + my_second
print("My combined tuples:", my_combined)

# My tuple in loop (5)
my_mountains = ("Blue Ridge", "Smoky", "Pisgah")
print("My mountains:")
for mountain in my_mountains:
    print("-", mountain)

# My sets - unique items only! (6)
my_set = {1, 2, 3, 4, 5}
