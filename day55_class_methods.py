# Day 55: static and class methods for my practice

class MyMath:
    pi = 3.14159
    
    @staticmethod
    def my_add(a, b):
        return a + b
    
    @staticmethod
    def my_multiply(a, b):
        return a * b
    
    @classmethod
    def my_circle_area(cls, radius):
        return cls.pi * radius ** 2

print(f"My add: {MyMath.my_add(5, 3)}")
print(f"My area: {MyMath.my_circle_area(5)}")

class MyPerson:
    count = 0
    
    def __init__(self, name):
        self.name = name
        MyPerson.count += 1
    
    @classmethod
    def my_total_count(cls):
        return cls.count
    
    @classmethod
    def my_from_string(cls, data_str):
        name = data_str.split(",")[0]
        return cls(name)

my_p1 = MyPerson("David")
my_p2 = MyPerson("Taylor")
print(f"My count: {MyPerson.my_total_count()}")

my_p3 = MyPerson.my_from_string("Alex,30")
print(f"My from string: {my_p3.name}")

class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def my_from_string(cls, date_str):
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)
    
    @staticmethod
    def my_is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

my_date = MyDate.my_from_string("2025-01-15")
print(f"My date: {my_date}")
print(f"My is leap: {MyDate.my_is_leap_year(2024)}")

class MyConfig:
    _instance = None
    
    @classmethod
    def my_get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

my_c1 = MyConfig.my_get_instance()
my_c2 = MyConfig.my_get_instance()
print(f"My same instance: {my_c1 is my_c2}")
