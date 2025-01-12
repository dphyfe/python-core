# Day 12: string formatting for my practice

# My basic info
my_name = "David"
my_city = "Asheville"
my_age = 30
my_temp = 55.5
my_pi = 3.14159

# My f-strings (easiest for me!) (1)
my_intro = f"My name is {my_name}"
print(my_intro)

my_full_intro = f"I am {my_name}, {my_age} years old, from {my_city}"
print(my_full_intro)

my_temp_string = f"Current temp: {my_temp:.1f} degrees"
print(my_temp_string)

# My f-string expressions (2)
my_doubled_age = f"Double my age: {my_age * 2}"
print(my_doubled_age)

my_length = f"My name has {len(my_name)} letters"
print(my_length)

my_calculation = f"10 + 5 = {10 + 5}"
print(my_calculation)

# My f-string with method calls (3)
my_upper_name = f"My name in caps: {my_name.upper()}"
print(my_upper_name)

my_lower_city = f"My city lowercase: {my_city.lower()}"
print(my_lower_city)

# My number formatting (4)
my_formatted_pi = f"Pi: {my_pi:.2f}"
print(my_formatted_pi)

my_formatted_pi2 = f"Pi to 4 decimals: {my_pi:.4f}"
print(my_formatted_pi2)

# My comma separators (5)
my_big_number = 1000000
my_formatted_big = f"Population: {my_big_number:,}"
print(my_formatted_big)

my_money = 12345.67
my_formatted_money = f"Amount: ${my_money:,.2f}"
