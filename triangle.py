class Triangle:
    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise Exception('треугольник не существует')



    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        __p = self.perimeter()/2
        return (__p*(__p-self.a)*(__p-self.b)*(__p-self.c))**0.5


tr = Triangle(3, 3, 3)
print(tr.perimeter())
print(tr.area())
