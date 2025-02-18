# Day 47: debugging techniques for my practice

import pdb

my_nums = [1, 2, 3, 4, 5]
# pdb.set_trace()  # Uncomment for debugging
my_sum = sum(my_nums)
print(f"My sum: {my_sum}")

def my_buggy(x):
    print(f"My input: {x}")
    result = x * 2
    print(f"My output: {result}")
    return result

my_buggy(5)

my_data = {"name": "David", "age": 30}
print(f"My data: {my_data}")

import logging
logging.basicConfig(level=logging.DEBUG)
my_logger = logging.getLogger(__name__)
my_logger.debug("My debug message")
my_logger.info("My info message")

def my_divide(a, b):
    try:
        result = a / b
        my_logger.info(f"My division: {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        my_logger.error("My division by zero error")
        return None

my_divide(10, 2)
my_divide(10, 0)

my_list = [1, 2, 3]
try:
    my_value = my_list[5]
except IndexError as e:
    print(f"My error: {e}")
    
import traceback
try:
    1 / 0
except:
    print("My traceback:")
    traceback.print_exc()
