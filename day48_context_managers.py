# Day 48: context managers for my practice

with open("test.txt", "w") as my_file:
    my_file.write("My test data")
print("My file closed automatically")

class MyResource:
    def __enter__(self):
        print("My enter called")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("My exit called")
        return False
    
    def my_do_something(self):
        print("My doing something")

with MyResource() as my_res:
    my_res.my_do_something()

from contextlib import contextmanager

@contextmanager
def my_context():
    print("My setup")
    yield "my value"
    print("My teardown")

with my_context() as my_val:
    print(f"My value: {my_val}")

import time
class MyTimer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        print(f"My elapsed: {self.end - self.start:.4f}s")

with MyTimer():
    sum(range(1000000))

from contextlib import suppress
with suppress(ValueError):
    int("not a number")
print("My error suppressed")

class MyConnection:
    def __enter__(self):
        print("My connection opened")
        return self
    
    def __exit__(self, *args):
        print("My connection closed")

with MyConnection() as my_conn:
    print("My working with connection")

# Progress: part 2/2
