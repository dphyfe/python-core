# Day 02: more strings and numbers (still beginner, no loops yet)

first_name = "David"
last_name = "Phyfe"
city = "Asheville"
state = "North Carolina"
hobby = "hiking"
pets = "dogs"
weather = "sunny"
terrain = "mountains"
food = "tacos"
mood = "curious"

# Combine strings in a few different ways.
full_name = first_name + " " + last_name
home_line = city + ", " + state
activity_line = "I enjoy " + hobby + " in the " + terrain
pet_line = "I like " + pets
weather_line = "Today's weather: " + weather
food_line = "Favorite food: " + food

print("Full name:", full_name)
print("Home:", home_line)
print(activity_line)
print(pet_line)
print(weather_line)
print(food_line)
print("Mood:", mood)

# String methods without loops.
print("Upper name:", full_name.upper())
print("Lower city:", city.lower())
print("Title state:", state.title())
print("Does hobby start with 'h'?", hobby.startswith("h"))
print("Does terrain end with 's'?", terrain.endswith("s"))

# Simple number practice.
days_coding = 2
hours_today = 1.5
hours_total = 2 + 1.5
breaks_taken = 2
ratio_work_break = hours_today / breaks_taken

print("Days coding so far:", days_coding)
print("Hours today:", hours_today)
print("Hours total estimate:", hours_total)
print("Breaks taken:", breaks_taken)
print("Work/break ratio:", ratio_work_break)

# A tiny concatenated summary.
summary = "Day " + str(days_coding) + " | " + full_name + " | " + home_line + " | Topic: strings and numbers"
print(summary)
