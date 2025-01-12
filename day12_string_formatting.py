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
print(my_formatted_money)

# My multiline strings (6)
my_paragraph = f"""
My name is {my_name}.
I live in {my_city}.
I am {my_age} years old.
"""
print(my_paragraph)

# My string with conditionals (7)
my_status = "adult" if my_age >= 18 else "minor"
my_status_text = f"I am an {my_status}"
print(my_status_text)

my_temp_status = "warm" if my_temp > 60 else "cool"
my_weather = f"It is {my_temp_status} today at {my_temp:.1f}Â°F"
print(my_weather)

# My dictionary formatting (8)
my_person = {"name": "David", "city": "Asheville", "state": "NC"}
my_dict_text = f"Info: {my_person['name']} from {my_person['city']}"
print(my_dict_text)

# My list in f-string (9)
my_mountains = ["Blue Ridge", "Smoky", "Pisgah"]
my_mountain_text = f"First mountain: {my_mountains[0]}"
print(my_mountain_text)

my_list_info = f"I have {len(my_mountains)} mountains in my list"
print(my_list_info)

# My join in f-string (10)
my_foods = ["tacos", "pizza", "noodles"]
my_foods_text = f"My favorite foods: {', '.join(my_foods)}"
print(my_foods_text)

# My complex expressions (11)
my_scores = [85, 90, 78, 92]
my_average = f"My average score: {sum(my_scores) / len(my_scores):.1f}"
print(my_average)

my_max_score = f"My best score: {max(my_scores)}"
print(my_max_score)

# My padding and alignment (12)
print(f"{'Name':<15} {'Age':>5} {'City':<15}")
print(f"{my_name:<15} {my_age:>5} {my_city:<15}")

# Progress: part 2/2
