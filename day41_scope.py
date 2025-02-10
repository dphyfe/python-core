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
my_a = "global"

def my_test():
    my_a = "local"
    print(f"My local a: {my_a}")

my_test()
print(f"My global a: {my_a}")

# My global modification (5)
my_list = [1, 2, 3]

def my_append():
    my_list.append(4)

my_append()
print(f"My list: {my_list}")

# My nested scope (6)
def my_level1():
    my_var = "level1"
    
    def my_level2():
        print(f"My from level2: {my_var}")
    
    my_level2()

my_level1()

# My global access (7)
my_config = {"debug": True}

def my_check_debug():
    if my_config["debug"]:
        print("My debug mode on")

my_check_debug()

# My multiple globals (8)

# Progress: part 2/3
