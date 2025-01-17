# Day 17: inheritance and polymorphism for my practice

# My base class (1)
class MyVehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def my_description(self):
        return f"{self.brand} {self.model}"

# My car class (inherits from Vehicle) (2)
class MyCar(MyVehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def my_description(self):
        return f"{super().my_description()} with {self.doors} doors"

my_car = MyCar("Toyota", "Camry", 4)
print(my_car.my_description())

# My motorcycle class (3)
class MyMotorcycle(MyVehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar
    
    def my_description(self):
        extra = " with sidecar" if self.has_sidecar else ""
        return f"{super().my_description()}{extra}"

my_bike = MyMotorcycle("Harley", "Street 750", False)
print(my_bike.my_description())

# My shape class with polymorphism (4)
class MyShape:
    def my_area(self):
        raise NotImplementedError("Subclass must implement my_area")

class MyRectangle(MyShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def my_area(self):
        return self.width * self.height

class MyCircle(MyShape):
    def __init__(self, radius):
        self.radius = radius
    
    def my_area(self):
        return 3.14 * self.radius * self.radius

# Polymorphism in action
my_shapes = [MyRectangle(5, 4), MyCircle(3)]
for shape in my_shapes:
    print(f"My area: {shape.my_area()}")

# My employee class (5)
class MyEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def my_raise(self, amount):
        self.salary += amount

class MyManager(MyEmployee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def my_info(self):
        return f"{self.name} manages {self.team_size} people"

my_emp = MyEmployee("Alice", 50000)
my_mgr = MyManager("Bob", 70000, 5)
print(my_mgr.my_info())
my_mgr.my_raise(10000)
print(f"New salary: {my_mgr.salary}")

# My multiple inheritance (6)
class MyWalker:
    def my_walk(self):
        return "I'm walking"

class MySwimmer:
    def my_swim(self):
        return "I'm swimming"

class MyDuck(MyWalker, MySwimmer):
    pass

my_duck = MyDuck()
print(my_duck.my_walk())
print(my_duck.my_swim())

# My super() with multiple inheritance (7)
class MyBase1:
    def my_method(self):
        return "Base1"

class MyBase2:
    def my_method(self):
        return "Base2"

class MyDerived(MyBase1, MyBase2):
    def my_method(self):
        return f"{super().my_method()} -> Derived"

my_derived = MyDerived()
print(my_derived.my_method())

# My isinstance and issubclass (8)
class MyAnimal:
    pass

class MyDog3(MyAnimal):
    pass

my_dog3 = MyDog3()
print(f"Is dog3 a MyDog3? {isinstance(my_dog3, MyDog3)}")
print(f"Is dog3 a MyAnimal? {isinstance(my_dog3, MyAnimal)}")
print(f"Is MyDog3 subclass of MyAnimal? {issubclass(MyDog3, MyAnimal)}")

# My abstract class with abc (9)
from abc import ABC, abstractmethod

class MyPaymentMethod(ABC):
    @abstractmethod
    def my_pay(self, amount):
        pass

class MyCreditCard(MyPaymentMethod):
    def my_pay(self, amount):
        return f"Paid {amount} with credit card"

class MyPayPal(MyPaymentMethod):
    def my_pay(self, amount):
        return f"Paid {amount} with PayPal"

my_payment1 = MyCreditCard()
my_payment2 = MyPayPal()
print(my_payment1.my_pay(100))
print(my_payment2.my_pay(50))

# My method override (10)
class MyPrinter:
    def my_print(self):
        return "Generic print"

class MyLaserPrinter(MyPrinter):
    def my_print(self):
        return "Laser print - high quality"

class MyInkPrinter(MyPrinter):
    def my_print(self):
        return "Ink print - standard quality"

my_printers = [MyLaserPrinter(), MyInkPrinter()]
for printer in my_printers:
    print(printer.my_print())
