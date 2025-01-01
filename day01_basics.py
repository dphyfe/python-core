# Day 01: first Python steps
# Basic prints and simple variables to verify the toolchain works.

print("Hello, Python! This is day 01.")

# Practice variables with plenty of examples (junior style).
first_name = "David"
last_name = "Phyfe"
full_name = first_name + " " + last_name
home = "Asheville, NC"
city = "Asheville"
state = "NC"
state_long = "North Carolina"
area = "Mountains"
hobby = "hiking"
pet_pref = "dogs"
days_coding = 1

print("Name:", full_name)
print("Home:", home)
print("City:", city)
print("State (short):", state)
print("State (long):", state_long)
print("Area:", area)
print("Hobby:", hobby)
print("Pet preference:", pet_pref)
print("Days coding so far:", days_coding)

# Early topics written as separate variables (no loops yet).
topic1 = "variables"
topic2 = "strings"
topic3 = "math"
print("Topics covered today:")
print("-", topic1)
print("-", topic2)
print("-", topic3)

# Things enjoyed back home as simple variables (no lists yet).
enjoy1 = "dogs"
enjoy2 = "mountains"
enjoy3 = "hiking"
enjoy4 = "outdoors"
print("Things I enjoy back home:")
print("-", enjoy1)
print("-", enjoy2)
print("-", enjoy3)
print("-", enjoy4)

# Simple math practice with several small examples.
apples = 2
oranges = 3
bananas = 4
pears = 1
fruit_total = apples + oranges + bananas + pears
fruit_diff = bananas - apples
double_apples = apples * 2
half_oranges = oranges / 2
mod_example = bananas % apples
floor_div = bananas // apples

print("Fruit total:", fruit_total)
print("Fruit difference (bananas - apples):", fruit_diff)
print("Double apples:", double_apples)
print("Half oranges:", half_oranges)
print("Bananas mod apples:", mod_example)
print("Bananas floor-div apples:", floor_div)

# String practice inserting variables (still simple).
greeting = f"Hi, I'm {full_name} from {city}, {state}."
intro = f"I like {hobby} in the {area}."
pet_line = f"I prefer {pet_pref}."
home_line = f"Home base: {home}."
city_state_line = f"City: {city}, State: {state_long}."
caps_greeting = greeting.upper()
lower_intro = intro.lower()
combined = greeting + " " + intro + " " + pet_line

print(greeting)
print(intro)
print(pet_line)
print(home_line)
print(city_state_line)
print("Greeting length:", len(greeting))
print("Caps greeting:", caps_greeting)
print("Lower intro:", lower_intro)
print("Combined line:", combined)

# Simple summary string without functions yet.
summary = "Day " + str(days_coding) + ": practiced " + topic1
print(summary)

# Progress: part 2/2
