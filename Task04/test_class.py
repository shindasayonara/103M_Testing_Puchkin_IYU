try:
    import pytest
except ImportError:
    print("pytest не установлен. Для запуска тестов выполните: pip install pytest")
    exit()

from triangle_class import Triangle, IncorrectTriangleSides


def test_create_triangle():
    t = Triangle(3, 4, 5)
    assert t.a == 3


def test_equilateral():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"


def test_isosceles():
    t = Triangle(3, 3, 4)
    assert t.triangle_type() == "isosceles"


def test_nonequilateral():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"


def test_perimeter():
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12


def test_invalid_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)


def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-3, 4, 5)