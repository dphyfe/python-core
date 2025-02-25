# Day 54: property decorators for my practice

class MyCircle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

my_circle = MyCircle(5)
print(f"My radius: {my_circle.radius}")
print(f"My area: {my_circle.area}")
my_circle.radius = 10
print(f"My new area: {my_circle.area}")

class MyPerson:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.first_name = first
        self.last_name = last

my_person = MyPerson("David", "Taylor")
print(f"My full name: {my_person.full_name}")
my_person.full_name = "John Smith"
