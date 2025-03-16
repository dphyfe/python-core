# Day 73: __name__ and __main__ for my practice

print(f"My module name: {__name__}")

def my_function():
    print("My function called")
    return "my result"

def my_main():
    print("My main function running")
    my_result = my_function()
    print(f"My result: {my_result}")

if __name__ == "__main__":
    print("My script running directly")
    my_main()
