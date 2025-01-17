import pytest
from Lesson17_Hw.app.app import add, divide, subtract, multiply


def test_add():
    """Тестирует функцию сложения."""
    assert add(2, 8) == 10
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    """Тестирует функцию деления."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
         divide(5, 0)

def test_subtract():
    """Возвращает разность двух чисел"""
    assert subtract(10,5) == 5
    assert subtract(0,0) == 0
    assert subtract(-6,3) == -9

def test_multiply():
    """Возвращает произвдение двух чисел"""
    assert multiply(5,5) == 25
    assert multiply(8,0) == 0
    assert multiply(-6,5) == -30





