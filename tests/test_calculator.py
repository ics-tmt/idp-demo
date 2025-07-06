import pytest
import calculator


def test_add():
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0.5, 0.5) == 1.0


def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5


def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0, 100) == 0


def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(9, 2) == 4.5


def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        calculator.divide(1, 0)
    assert str(excinfo.value) == 'Cannot divide by zero'