import pytest
from calculator import add, subtract, multiply, divide, is_even

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 5) == 5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, -2) == -2.5
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True

def test_main_even_and_odd():
    import sys
    import subprocess

    # Test with an even input
    result = subprocess.run(
        [sys.executable, 'calculator.py'], input='4\n', text=True, capture_output=True
    )
    assert '4 is even.' in result.stdout

    # Test with an odd input
    result = subprocess.run(
        [sys.executable, 'calculator.py'], input='3\n', text=True, capture_output=True
    )
    assert '3 is odd.' in result.stdout

def test_main_invalid_input():
    import sys
    import subprocess

    result = subprocess.run(
        [sys.executable, 'calculator.py'], input='abc\n', text=True, capture_output=True
    )
    assert 'Invalid input; please enter an integer.' in result.stdout