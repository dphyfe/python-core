# Day 07: first dictionaries for my practice

# My person dictionary
person = {
    "name": "David",
    "city": "Asheville",
    "hobby": "hiking",
}

print("My person dict:", person)
print("My name:", person["name"])
print("My city:", person.get("city"))

# Adding a new key to my dict (1)
person["pet"] = "dog"
print("My dict with pet:", person)

# Adding another key
person["age"] = 30
print("My dict with age:", person)

# Updating a value in my dict (2)
person["hobby"] = "trail running"
print("My updated hobby:", person)

# Updating my city
person["city"] = "Asheville, NC"
print("My updated city:", person)

# Check if a key exists in my dict (3)
print("Do I have a car key?", "car" in person)
print("Do I have a pet key?", "pet" in person)
print("Do I have a name key?", "name" in person)

# Use get with my default value (4)
car = person.get("car", "no car yet")
print("My car:", car)

job = person.get("job", "learning to code")
print("My job:", job)

# Remove a key from my dict (5)
removed_hobby = person.pop("hobby")
print("I removed hobby:", removed_hobby)
print("My dict after removal:", person)

# Add multiple keys to my dict with update (6)
person.update({"hobby": "climbing", "state": "NC"})
print("My dict after update:", person)

# Another update for my practice
person.update({"favorite_season": "fall"})
print("My dict with season:", person)

# Loop over keys in my dict (7)
print("My keys:")
for key in person:
    print("-", key)

# Loop over keys and values in my dict
print("My keys and values:")
for key in person:
    print(key + ":", person[key])

# Loop using items in my dict (8)
for key, value in person.items():
    print("My item:", key, "->", value)

# Getting all my keys
my_keys = person.keys()
print("All my keys:", list(my_keys))

# Getting all my values
my_values = person.values()
print("All my values:", list(my_values))

# Creating another dict for my dogs
dogs = {
    "name1": "Scout",
    "name2": "Luna",
    "breed": "mixed",
}
print("My dogs dict:", dogs)

# Nested dictionary for my profile (9)
profile = {
    "person": person,
    "favorites": {
        "mountain": "Blue Ridge",
        "food": "tacos",
    },
}
print("My nested profile:", profile)
print("My favorite mountain:", profile["favorites"]["mountain"])
print("My favorite food:", profile["favorites"]["food"])

# Another nested dict for my activities
my_week = {
    "weekday": {
        "activity": "coding",
        "hours": 4,
    },
    "weekend": {
        "activity": "hiking",
        "hours": 6,
    },
}
print("My weekly schedule:", my_week)
print("My weekday activity:", my_week["weekday"]["activity"])
print("My weekend hours:", my_week["weekend"]["hours"])

# Creating a dict from scratch with my hobbies
hobbies = {}
hobbies["outdoor"] = "hiking"
hobbies["indoor"] = "reading"
hobbies["creative"] = "writing"
print("My hobbies dict:", hobbies)

# Checking length of my dict
print("My person dict has", len(person), "keys")
print("My hobbies dict has", len(hobbies), "keys")

# Copying my dict
person_backup = person.copy()
print("My backup dict:", person_backup)

# Clearing a temporary dict
temp_dict = {"a": 1, "b": 2}
print("My temp dict before clear:", temp_dict)
temp_dict.clear()
print("My temp dict after clear:", temp_dict)

# Using setdefault on my dict
person.setdefault("country", "USA")
print("My person with country:", person)
person.setdefault("name", "Default Name")  # won't change existing
print("My person name unchanged:", person["name"])
