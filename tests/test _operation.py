from src.math_operations import add, sub 

def test_add():
    assert add(4,5) == 9
    assert add(1,3) == 5

def test_sub():
    assert sub(5,2) == 3
    assert sub(5,3) == 1