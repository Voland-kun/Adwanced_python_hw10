class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        __p = self.perimeter()/2
        return (__p*(__p-self.a)*(__p-self.b)*(__p-self.c))**0.5


tr = Triangle(3, 3, 3)
print(tr.perimeter())
print(tr.area())
