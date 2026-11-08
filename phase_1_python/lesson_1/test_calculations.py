from calculations import add

def test_add_positive():
    assert add(5, 12) == 17

def test_add_negative():
    assert add(-4, 25) == 21

def test_add_zero():
    assert add(21, 0) == 21