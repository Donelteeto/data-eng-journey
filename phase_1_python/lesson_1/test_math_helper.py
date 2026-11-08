from math_helper import multiply

def test_multiply_positive_numbers():
    assert multiply(5, 8) == 40

def test_multiply_by_zero():
    assert multiply(2, 0) == 0
