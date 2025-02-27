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
print(f"My equal: {my_v1 == my_v2}")

class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __contains__(self, item):
        return item in self.items

my_list = MyList([1, 2, 3, 4, 5])
print(f"My length: {len(my_list)}")
print(f"My item: {my_list[2]}")
print(f"My contains: {3 in my_list}")

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

for my_num in MyRange(1, 5):
    print(f"My num: {my_num}")

class MyContext:
    def __enter__(self):
        print("My entering")
        return self
    
    def __exit__(self, *args):
        print("My exiting")

with MyContext():
    print("My inside context")

class MyCallable:
    def __call__(self, x):
        return x * 2

my_func = MyCallable()
print(f"My called: {my_func(5)}")

# Progress: part 2/2
