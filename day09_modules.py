# Day 09: using standard library modules for my practice

import math
import random
import statistics
from datetime import date, datetime, timedelta

# My math examples
my_number = 9
my_sqrt = math.sqrt(my_number)
print("My square root of", my_number, "is", my_sqrt)

# Another square root for my practice
print("Square root of 16:", math.sqrt(16))
print("Square root of 25:", math.sqrt(25))

# My angle calculations
my_angle = 45
my_radians = math.radians(my_angle)
print("My sin(45 degrees):", math.sin(my_radians))
print("My cos(45 degrees):", math.cos(my_radians))

# More math examples for my learning (1-5)
print("My 2 to the power of 3:", math.pow(2, 3))
print("My 5 to the power of 2:", math.pow(5, 2))
print("My floor of 3.9:", math.floor(3.9))
print("My floor of 7.2:", math.floor(7.2))
print("My ceil of 3.1:", math.ceil(3.1))
print("My ceil of 8.01:", math.ceil(8.01))

# My absolute value practice
print("My abs of -10:", math.fabs(-10))
print("My abs of -3.5:", math.fabs(-3.5))

# Random examples for my practice (6-10)
print("My random integer 1-10:", random.randint(1, 10))
print("My random integer 50-100:", random.randint(50, 100))
print("My random choice from animals:", random.choice(["dog", "cat", "bird"]))
print("My random choice from mountains:", random.choice(["Blue Ridge", "Smoky", "Pisgah"]))

# Shuffling my list
my_numbers = [1, 2, 3, 4, 5]
random.shuffle(my_numbers)
print("My shuffled numbers:", my_numbers)

# Shuffling again
my_foods = ["tacos", "pizza", "noodles"]
random.shuffle(my_foods)
print("My shuffled foods:", my_foods)

# Random samples from my lists
print("My two random trails:", random.sample(["trail", "river", "park", "forest"], 2))
print("My three random activities:", random.sample(["hike", "code", "read", "cook", "walk"], 3))

# My random float practice
print("My random float 0-1:", random.random())
print("My random uniform 1-10:", random.uniform(1, 10))

# Statistics examples for my practice (11)
my_values = [2, 4, 6, 8, 10]
print("My mean of values:", statistics.mean(my_values))

# More statistics
my_scores = [85, 90, 78, 92, 88]
print("My mean score:", statistics.mean(my_scores))
print("My median score:", statistics.median(my_scores))

# Another stats example
my_temps = [55, 60, 58, 62, 59]
print("My average temp:", statistics.mean(my_temps))

# Date formatting examples for my practice (12)
my_date = date(2025, 1, 9)
print("My formatted date:", my_date.isoformat())
print("My date year:", my_date.year)
print("My date month:", my_date.month)
print("My date day:", my_date.day)

# Creating more dates
my_birthday = date(1990, 5, 15)
print("My birthday:", my_birthday)

# Using datetime
my_now = datetime(2025, 1, 9, 10, 30, 0)
print("My datetime:", my_now)
print("My datetime hour:", my_now.hour)

# My timedelta practice
my_tomorrow = my_date + timedelta(days=1)
print("My tomorrow:", my_tomorrow)

my_next_week = my_date + timedelta(weeks=1)
print("My next week:", my_next_week)

# Rounding examples for my practice
my_pi = 3.14159
print("My rounded pi to 2 decimals:", round(my_pi, 2))
print("My rounded pi to 3 decimals:", round(my_pi, 3))

my_value = 7.89543
print("My rounded value to 1 decimal:", round(my_value, 1))

# My constant practice
print("My pi constant:", math.pi)
print("My e constant:", math.e)

# My logarithm practice
print("My log of 10:", math.log10(10))
print("My natural log of e:", math.log(math.e))

# My factorial practice
print("My factorial of 5:", math.factorial(5))
print("My factorial of 3:", math.factorial(3))

# My trigonometry review
print("My tan(45 degrees):", math.tan(my_radians))

# Generating my random choices for hiking days
my_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
my_hike_day = random.choice(my_days)
print("My random hike day:", my_hike_day)

# My seed for reproducible random (just practicing)
random.seed(42)
print("My seeded random:", random.randint(1, 100))
random.seed(42)
print("My seeded random again (same):", random.randint(1, 100))
