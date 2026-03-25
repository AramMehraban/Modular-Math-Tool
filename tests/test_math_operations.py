import math_operations as math_ops

def test_add():
    assert math_ops.add(2, 3) == 5

def test_subtract():
    assert math_ops.subtract(5, 3) == 2

def test_multiply():
    assert math_ops.multiply(2, 4) == 8

def test_divide():
    assert math_ops.divide(10, 2) == 5
    assert math_ops.divide(5, 0) == "Fehler: Division durch Null!"