import pytest
from app.app import add, divide, subtract, multiply

@pytest.mark.parametrize("a, b, expected", [
    (2, 8, 10),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a,b) == expected



@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (5, 0, 0),
])
def test_divide(a, b, expected):
    if b == 0:
        with pytest.raises(ValueError):
         divide(a, b)
    else:
        assert divide(a, b) == expected

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (0, 0, 0),
    (-6, 3, -9),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 25),
    (8, 0, 0),
    (-6, 5, -30),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


