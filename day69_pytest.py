# Day 69: pytest basics for my practice

def my_add(a, b):
    return a + b

def my_multiply(a, b):
    return a * b

def my_divide(a, b):
    if b == 0:
        raise ValueError("My division by zero")
    return a / b

def test_my_add():
    assert my_add(2, 3) == 5
    assert my_add(-1, 1) == 0
    assert my_add(0, 0) == 0

def test_my_multiply():
    assert my_multiply(2, 3) == 6
    assert my_multiply(-2, 3) == -6
    assert my_multiply(0, 5) == 0

def test_my_divide():
    assert my_divide(10, 2) == 5
    assert my_divide(9, 3) == 3

def test_my_divide_by_zero():
    try:
        my_divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "division by zero" in str(e)

import pytest

def test_my_with_pytest():
    with pytest.raises(ValueError):
        my_divide(1, 0)

@pytest.fixture
def my_sample_data():
    return [1, 2, 3, 4, 5]

def test_my_fixture(my_sample_data):
    assert len(my_sample_data) == 5
    assert sum(my_sample_data) == 15

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
