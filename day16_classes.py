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
