# Day 41: scope and global for my practice

my_global_var = "global"

def my_function():
    my_local_var = "local"
    print(f"My local: {my_local_var}")
    print(f"My global from func: {my_global_var}")

my_function()

# My global keyword (2)
my_counter = 0

def my_increment():
    global my_counter
    my_counter += 1

my_increment()
my_increment()
print(f"My counter: {my_counter}")

# My nonlocal (3)
def my_outer():
    my_x = "outer"
    
    def my_inner():
        nonlocal my_x
        my_x = "inner"
    
    my_inner()
    print(f"My x: {my_x}")

my_outer()

# My scope hierarchy (4)
