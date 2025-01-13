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
print("My set:", my_set)

my_colors_set = {"blue", "green", "red"}
print("My colors set:", my_colors_set)

# My set from list (removes duplicates) (7)
my_with_dupes = [1, 2, 2, 3, 3, 3, 4]
my_unique_set = set(my_with_dupes)
print("My unique set:", my_unique_set)

# Another duplicate removal
my_words = ["dog", "cat", "dog", "bird", "cat"]
my_unique_words = set(my_words)
print("My unique words:", my_unique_words)

# My set operations - adding (8)
my_activities = {"hiking", "coding"}
my_activities.add("reading")
print("My activities after add:", my_activities)

my_activities.add("hiking")  # won't add duplicate
print("My activities after adding duplicate:", my_activities)

# My set removing items (9)
my_numbers_set = {1, 2, 3, 4, 5}
my_numbers_set.remove(3)
print("My set after remove:", my_numbers_set)

my_numbers_set.discard(10)  # won't error if not found
print("My set after discard:", my_numbers_set)

# My set union (10)
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_union = my_set1 | my_set2

# Progress: part 2/3
