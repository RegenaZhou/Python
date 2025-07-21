from my_calculator import my_adder

def test_positive_with_positive():
    assert my_adder(3,5) == 8

def test_negative_with_positive():
    assert my_adder(-3,5) == 2