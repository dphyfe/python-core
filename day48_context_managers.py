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
