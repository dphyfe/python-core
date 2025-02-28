# Day 57: operator overloading for my practice

class MyFraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return MyFraction(new_num, new_den)
    
    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return MyFraction(new_num, new_den)
    
    def __mul__(self, other):
        return MyFraction(self.num * other.num, self.den * other.den)
    
    def __truediv__(self, other):
        return MyFraction(self.num * other.den, self.den * other.num)
    
    def __str__(self):
        return f"{self.num}/{self.den}"

my_f1 = MyFraction(1, 2)
my_f2 = MyFraction(1, 3)
print(f"My sum: {my_f1 + my_f2}")
print(f"My product: {my_f1 * my_f2}")

class MyComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def __str__(self):
        return f"{self.real}+{self.imag}i"

my_c1 = MyComplex(3, 4)
my_c2 = MyComplex(1, 2)
print(f"My sum: {my_c1 + my_c2}")
print(f"My abs: {abs(my_c1)}")
print(f"My less: {my_c2 < my_c1}")

class MyMatrix:
    def __init__(self, data):
        self.data = data
    
    def __matmul__(self, other):
        result = [[0] * len(other.data[0]) for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return MyMatrix(result)
    
    def __str__(self):
        return str(self.data)

my_m1 = MyMatrix([[1, 2], [3, 4]])
my_m2 = MyMatrix([[5, 6], [7, 8]])
my_result = my_m1 @ my_m2
print(f"My product: {my_result}")
