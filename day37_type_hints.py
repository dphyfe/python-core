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
print(f"My processed: {my_processed}")

def my_person(name: str, age: int) -> Dict[str, int]:
    return {"name": name, "age": age}

my_data: Dict[str, int] = my_person("David", 30)
print(f"My person: {my_data}")

def my_optional(value: Optional[str]) -> Optional[int]:
    if value:
        return len(value)
    return None

my_len: Optional[int] = my_optional("hello")
print(f"My optional: {my_len}")

def my_tuple(a: int, b: str) -> Tuple[int, str]:
    return (a, b)

my_tuple_result: Tuple[int, str] = my_tuple(42, "answer")
print(f"My tuple: {my_tuple_result}")

from typing import Union

def my_flexible(value: Union[int, str]) -> str:
    return str(value)

print(f"My flexible int: {my_flexible(42)}")

# Progress: part 2/3
