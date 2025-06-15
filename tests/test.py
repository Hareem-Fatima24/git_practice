from src.mathoperations import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-2,8) == 6
    assert add(-2,-2)== -4
def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-2,8) == -10
    assert subtract(-2,-2)== 0