# Day 37: type hints for my practice

def my_add(a: int, b: int) -> int:
    return a + b

my_result: int = my_add(5, 3)
print(f"My result: {my_result}")

from typing import List, Dict, Tuple, Optional

def my_process(items: List[int]) -> List[int]:
    return [x * 2 for x in items]

my_nums: List[int] = [1, 2, 3]
my_processed: List[int] = my_process(my_nums)
