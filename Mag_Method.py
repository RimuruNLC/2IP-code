class Test:
    def __init__(self,age):
        self.age = age
    def __add__(self, other):
        return self.age + other
    def __sub__(self, other):
        return self.age - other
    def __mul__(self, other):
        return self.age * other
    def __truediv__(self, other):
        return self.age / other
    def __floordiv__(self, other):
        return self.age // other
    def __pow__(self, power, modulo=None):
        return self.age ** power
    def __radd__(self, other):
        return other + self.age
    def __rsub__(self, other):
        return other - self.age
    def __rmul__(self, other):
        return other * self.age
    def __rtruediv__(self, other):
        return other / self.age
    def __rfloordiv__(self, other):
        return other // self.age
    def __rpow__(self, other):
        return other ** self.age
    def __iadd__(self, other):
        self.age += other
        return self
    def __isub__(self, other):
        self.age -= other
        return self
    def __imul__(self, other):
        self.age *= other
        return self
    def __itruediv__(self, other):
        self.age /= other
        return self
    def __ifloordiv__(self, other):
        self.age //= other
        return self
    def __lt__(self, other):
        return self.age < other
    def __le__(self, other):
        return self.age <= other
    def __eq__(self, other):
        return self.age == other
    def __ne__(self, other):
        return self.age != other
    def __ge__(self, other):
        return self.age >= other
    def __gt__(self, other):
        return self.age > other
abube = Test(18)
print(abube>=18)
