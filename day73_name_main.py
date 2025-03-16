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
else:
    print("My script imported as module")

class MyClass:
    def __init__(self):
        self.name = "MyClass"
    
    def my_method(self):
        print(f"My method from {self.name}")

def my_helper():
    return "my helper result"

if __name__ == "__main__":
    print("\nMy testing code:")
    my_obj = MyClass()
    my_obj.my_method()
    print(f"My helper: {my_helper()}")

my_module_level_var = "my module variable"

def my_show_vars():
    print(f"My module var: {my_module_level_var}")

if __name__ == "__main__":
    print("\nMy variables:")
    my_show_vars()
    print(f"My globals count: {len(globals())}")
    print(f"My locals count: {len(locals())}")

print(f"\nMy __file__: {__file__ if '__file__' in globals() else 'not defined'}")

if __name__ == "__main__":
    print("\nMy command line interface example:")
    import sys
    my_args = sys.argv
    print(f"My script name: {my_args[0] if my_args else 'none'}")
    print(f"My arguments: {my_args[1:] if len(my_args) > 1 else 'none'}")

if __name__ == "__main__":
    print("\nMy typical main pattern:")
    print("  def main():")
    print("      # My main logic")
    print("      pass")
    print("")
    print("  if __name__ == '__main__':")
    print("      main()")

# Progress: part 3/3
