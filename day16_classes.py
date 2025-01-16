# Day 16: classes and objects for my practice

# My first class (1)
class MyDog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def my_bark(self):
        return f"{self.name} says woof!"

# Creating my dog objects
my_scout = MyDog("Scout", 3)
my_luna = MyDog("Luna", 5)

print(my_scout.name)
print(my_scout.my_bark())
print(my_luna.my_bark())

# My class with multiple methods (2)
class MyPerson:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.hobbies = []
    
    def my_add_hobby(self, hobby):
        self.hobbies.append(hobby)
    
    def my_info(self):
        return f"{self.name} from {self.city}"
    
    def my_list_hobbies(self):
        return f"My hobbies: {', '.join(self.hobbies)}"

# Creating my person
my_david = MyPerson("David", "Asheville")
my_david.my_add_hobby("hiking")
my_david.my_add_hobby("coding")
print(my_david.my_info())
print(my_david.my_list_hobbies())

# My class with attributes (3)
class MyBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read_pages = 0
    
    def my_read(self, num_pages):
        self.read_pages += num_pages
    
    def my_progress(self):
        percent = (self.read_pages / self.pages) * 100
        return f"{percent:.1f}%"

# Reading my book
my_book = MyBook("Python Basics", "John Doe", 300)
my_book.my_read(75)
my_book.my_read(75)
print(f"Progress: {my_book.my_progress()}")

# My class methods (static) (4)
class MyMath:
    @staticmethod
    def my_add(a, b):
        return a + b
    
    @staticmethod
    def my_multiply(a, b):
        return a * b

print("My static add:", MyMath.my_add(5, 3))
print("My static multiply:", MyMath.my_multiply(4, 7))

# My class variable (shared across instances) (5)
class MyCounter:
    my_count = 0
    
    def __init__(self, name):
        self.name = name
        MyCounter.my_count += 1
    
    def my_total(self):
        return f"Total counters: {MyCounter.my_count}"

my_c1 = MyCounter("first")
my_c2 = MyCounter("second")
my_c3 = MyCounter("third")
print(my_c1.my_total())

# My property decorator (6)
class MyTemperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def my_fahrenheit(self):
        return (self._celsius * 9/5) + 32

my_temp = MyTemperature(0)
print(f"0 Celsius = {my_temp.my_fahrenheit} Fahrenheit")

my_temp2 = MyTemperature(100)
print(f"100 Celsius = {my_temp2.my_fahrenheit} Fahrenheit")

# My class with __str__ (7)
class MyCity:
    def __init__(self, name, state):
        self.name = name
        self.state = state
    
    def __str__(self):
        return f"{self.name}, {self.state}"

my_asheville = MyCity("Asheville", "NC")
print("My city:", my_asheville)

# My class with __repr__ (8)
class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

my_point = MyPoint(3, 4)
print("My point repr:", repr(my_point))

# Progress: part 3/4
