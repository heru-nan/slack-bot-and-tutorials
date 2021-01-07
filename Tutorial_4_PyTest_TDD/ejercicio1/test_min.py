
import min

def test_get_min():
    v = [10,2,1,100,3,4,-10]
    assert min.get_min(v) == -10

def test_get_min2():
    v=[0, 30, 5, 6]
    assert min.get_min(v) == 0

