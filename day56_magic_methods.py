# Day 56: magic methods for my practice

class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"MyVector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"MyVector({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

my_v1 = MyVector(1, 2)
my_v2 = MyVector(3, 4)
my_v3 = my_v1 + my_v2
print(f"My sum: {my_v3}")
