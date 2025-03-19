# Day 75: __init__ and packages for my practice

print("My package concepts:")

my_package_structure = """
my_package/
    __init__.py          # My package initializer
    module1.py           # My module 1
    module2.py           # My module 2
    subpackage/
        __init__.py      # My subpackage init
        module3.py       # My module 3
"""
print(my_package_structure)

my_init_example = """
# My __init__.py example
from .module1 import MyClass1
from .module2 import my_function2
from .subpackage.module3 import MyClass3

__all__ = ['MyClass1', 'my_function2', 'MyClass3']
__version__ = '1.0.0'

print('My package initialized')
"""
print("My __init__.py content:")
print(my_init_example)

my_module1 = """
# My module1.py example
class MyClass1:
    def __init__(self):
        self.name = 'MyClass1'
    
    def my_method(self):
        return 'my result from class1'
"""
print("\nMy module1.py:")
print(my_module1)

my_usage = """
# My usage examples
import my_package
from my_package import MyClass1
from my_package.subpackage import MyClass3
"""
print("\nMy import usage:")
print(my_usage)

print("\nMy __init__.py purposes:")
print("  1. Make directory a package")
print("  2. Initialize package-level variables")
print("  3. Import submodules for convenience")
print("  4. Define __all__ for 'from package import *'")
print("  5. Execute package setup code")

print("\nMy __all__ example:")
my_all_example = """
__all__ = ['function1', 'Class1', 'CONSTANT']
"""
print(my_all_example)

print("\nMy relative imports:")
print("  from . import module")
print("  from .. import module")
print("  from .subpackage import module")

print("\nMy package best practices:")
print("  - Always include __init__.py")
print("  - Use __all__ to control exports")
print("  - Import commonly used items in __init__.py")
print("  - Use relative imports within package")
print("  - Document package structure in README")

my_metadata = {
    "name": "my_package",
    "version": "1.0.0",
    "author": "David",
    "description": "My example package"
}
print(f"\nMy package metadata: {my_metadata}")
