# Day 52: type checking with mypy for my practice

from typing import List, Dict, Optional, Union, Tuple

def my_greet(name: str) -> str:
    return f"Hello, {name}!"

print(my_greet("David"))

def my_add_numbers(a: int, b: int) -> int:
    return a + b

print(f"My sum: {my_add_numbers(5, 3)}")

def my_process_list(items: List[int]) -> int:
    return sum(items)

my_nums: List[int] = [1, 2, 3, 4, 5]
print(f"My processed: {my_process_list(my_nums)}")

def my_get_config() -> Dict[str, Union[str, int]]:
    return {"name": "David", "age": 30}

my_config: Dict[str, Union[str, int]] = my_get_config()
print(f"My config: {my_config}")

def my_find_user(user_id: int) -> Optional[str]:
    users = {1: "David", 2: "Taylor"}
    return users.get(user_id)

my_user: Optional[str] = my_find_user(1)
print(f"My user: {my_user}")

def my_swap(pair: Tuple[int, int]) -> Tuple[int, int]:
    a, b = pair
    return (b, a)

my_pair: Tuple[int, int] = (1, 2)
my_swapped: Tuple[int, int] = my_swap(my_pair)
print(f"My swapped: {my_swapped}")

from typing import Callable

def my_apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

def my_double(x: int) -> int:
    return x * 2

my_result: int = my_apply(my_double, 5)
print(f"My result: {my_result}")

class MyPerson:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

my_person: MyPerson = MyPerson("David", 30)
print(f"My person: {my_person.name}")
