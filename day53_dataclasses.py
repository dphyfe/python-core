# Day 53: dataclasses for my practice

from dataclasses import dataclass, field
from typing import List

@dataclass
class MyPerson:
    name: str
    age: int
    email: str = "unknown@example.com"

my_person = MyPerson("David", 30)
print(f"My person: {my_person}")
print(f"My name: {my_person.name}")

@dataclass
class MyPoint:
    x: float
    y: float

my_p1 = MyPoint(1.0, 2.0)
my_p2 = MyPoint(1.0, 2.0)
print(f"My equal: {my_p1 == my_p2}")

@dataclass(frozen=True)
class MyConfig:
    debug: bool
    timeout: int

my_config = MyConfig(True, 30)
print(f"My config: {my_config}")

@dataclass
class MyInventory:
    items: List[str] = field(default_factory=list)
    
my_inv1 = MyInventory()
my_inv2 = MyInventory()
my_inv1.items.append("apple")
print(f"My inv1: {my_inv1.items}")
print(f"My inv2: {my_inv2.items}")

@dataclass(order=True)
class MyScore:
    points: int
    name: str = field(compare=False)

my_scores = [MyScore(85, "David"), MyScore(90, "Taylor"), MyScore(80, "Alex")]
my_sorted = sorted(my_scores)
print(f"My sorted: {[s.name for s in my_sorted]}")

from dataclasses import asdict, astuple

my_data = MyPerson("David", 30)
my_dict = asdict(my_data)
my_tuple = astuple(my_data)
print(f"My dict: {my_dict}")
print(f"My tuple: {my_tuple}")

@dataclass
class MyProduct:
    name: str
    price: float
    quantity: int = 1
    
    @property
    def total(self) -> float:
        return self.price * self.quantity

my_product = MyProduct("Apple", 1.5, 10)
print(f"My total: {my_product.total}")
