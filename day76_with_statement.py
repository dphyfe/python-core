# Day 76: with statement for my practice

with open("my_temp.txt", "w") as f:
    f.write("My content")
print("My file written and closed")

with open("my_temp.txt", "r") as f:
    my_content = f.read()
    print(f"My read: {my_content}")

import os
os.remove("my_temp.txt")

class MyResource:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"My {self.name} acquired")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"My {self.name} released")
        return False
    
    def my_use(self):
        print(f"My using {self.name}")

with MyResource("resource1") as my_res:
    my_res.my_use()

print("\nMy multiple context managers:")
with open("my_file1.txt", "w") as f1, open("my_file2.txt", "w") as f2:
    f1.write("My file 1")
    f2.write("My file 2")
print("My both files written")

os.remove("my_file1.txt")
os.remove("my_file2.txt")

from contextlib import contextmanager

@contextmanager
