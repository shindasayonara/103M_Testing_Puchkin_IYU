class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника.

    >>> get_triangle_type(3, 3, 3)
    'equilateral'

    >>> get_triangle_type(3, 3, 4)
    'isosceles'

    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    """

    sides = sorted([a, b, c])

    if any(type(x) not in (int, float) for x in sides):
        raise IncorrectTriangleSides("Стороны должны быть числами")

    if any(x <= 0 for x in sides):
        raise IncorrectTriangleSides("Стороны должны быть положительными")

    if sides[0] + sides[1] <= sides[2]:
        raise IncorrectTriangleSides("Треугольник не существует")

    if a == b == c:
        return "equilateral"

    if a == b or b == c or a == c:
        return "isosceles"

    return "nonequilateral"