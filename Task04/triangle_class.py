class IncorrectTriangleSides(Exception):
    pass


class Triangle:

    def __init__(self, a, b, c):
        sides = sorted([a, b, c])

        if any(type(x) not in (int, float) for x in sides):
            raise IncorrectTriangleSides("Стороны должны быть числами")

        if any(x <= 0 for x in sides):
            raise IncorrectTriangleSides("Стороны должны быть положительными")

        if sides[0] + sides[1] <= sides[2]:
            raise IncorrectTriangleSides("Треугольник не существует")

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):

        if self.a == self.b == self.c:
            return "equilateral"

        if self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"

        return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c