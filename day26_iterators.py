# Day 26: iterators protocol for my practice

# My basic iterator (1)
class MyCountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        self.current += 1
        return self.current - 1

my_counter = MyCountUp(5)
for my_num in my_counter:
    print(f"My number: {my_num}")

# My iterator from list (2)
my_list = [1, 2, 3]
my_iter = iter(my_list)
print(f"My first: {next(my_iter)}")
print(f"My second: {next(my_iter)}")

# My iterator exception (3)
my_small = [1, 2]
my_iter = iter(my_small)
try:
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
except StopIteration:
    print("My iteration complete")

# My range iterator (4)
my_range = range(5)
my_iter = iter(my_range)
print(f"My value: {next(my_iter)}")

# My string iterator (5)
my_text = "hello"
for my_char in my_text:
    print(f"My char: {my_char}")

# My dict iterator (6)
my_dict = {"a": 1, "b": 2}
for my_key in my_dict:
    print(f"My key: {my_key}")

# My custom iterator class (7)
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        my_val = self.current
        self.current += 1
        return my_val

for my_num in MyRange(1, 4):
    print(f"My custom: {my_num}")

# My iterator with state (8)
class MyFibonacci:
    def __init__(self, max):
        self.max = max
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a >= self.max:
            raise StopIteration
        my_val = self.a
        self.a, self.b = self.b, self.a + self.b
        return my_val

for my_fib in MyFibonacci(10):
    print(f"My fib: {my_fib}")

# My infinite iterator (9)
class MyInfiniteCounter:
    def __init__(self):
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.count += 1
        return self.count

my_inf = MyInfiniteCounter()
for i, val in enumerate(my_inf):
    if i >= 3:
        break
    print(f"My infinite: {val}")

# My zip as iterator (10)
my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_zipped = zip(my_list1, my_list2)
for my_pair in my_zipped:
    print(f"My pair: {my_pair}")
