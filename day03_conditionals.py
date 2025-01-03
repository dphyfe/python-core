# Day 03: simple comparisons and if/else (still small steps)

name = "David"
city = "Asheville"
likes_dogs = True
likes_cats = False
age = 30
hours_slept = 7
hours_goal = 8
temperature = 55
rain_expected = False
has_hiking_boots = True
time_available_hours = 2
friends_in_town = True
has_coffee = False
trail_open = True
mountain_view_clear = True

print("Name:", name)
print("City:", city)

# My basic comparisons (1-4)
print("Age >= 18:", age >= 18)
print("Age < 21:", age < 21)
print("Slept enough:", hours_slept >= hours_goal)
print("Is it cold for me?", temperature < 40)

# My yes/no checks (5-6)
if likes_dogs:
    print("I like dogs.")
else:
    print("Not a dog person yet.")

if likes_cats:
    print("Cats are great.")
else:
    print("Not a cat person right now.")

# My sleep decision (7)
if hours_slept < hours_goal:
    print("I need more sleep.")
else:
    print("I slept enough today.")

# My weather call (8-9)
if temperature > 50 and not rain_expected:
    print("I feel good about walking outside.")

if temperature < 32 or rain_expected:
    print("I might stay inside today.")
else:
    print("No freezing temps and no rain, I can head out.")

# My gear/time check (10)
if has_hiking_boots and time_available_hours >= 2:
    print("I have boots and time for a short trail.")
else:
    print("I will keep it to a quick neighborhood walk.")

# My social decision (11)
if friends_in_town and has_coffee:
    print("I will meet friends for coffee.")
else:
    print("No coffee meetup right now.")

# My nested hometown pride (12)
if city == "Asheville":
    print("Home is Asheville.")
    if likes_dogs:
        print("Asheville + dogs = a good day for me.")
    else:
        print("Asheville without dogs today.")

# My trail decision (13)
if trail_open and mountain_view_clear:
    print("I can hike and enjoy the view.")
elif trail_open and not mountain_view_clear:
    print("Trail is open but the view is hazy; still going.")
else:
    print("Trail is closed; I will reschedule.")

# My short ternary-like choice (14)
plan = "walk the dogs" if likes_dogs else "read a book"
print("Today's simple plan:", plan)
