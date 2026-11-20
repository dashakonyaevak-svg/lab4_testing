import pytest
from math_module import factorial, is_even


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_factorial_larger_number():
    assert factorial(10) == 3628800


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)


def test_factorial_wrong_type():
    with pytest.raises(TypeError):
        factorial("5")


@pytest.mark.parametrize("n, expected", [
    (0, True), (1, False), (2, True), (-4, True), (-7, False), (101, False),
])
def test_is_even(n, expected):
    assert is_even(n) == expected


def test_is_even_wrong_type():
    with pytest.raises(TypeError):
        is_even(2.5)