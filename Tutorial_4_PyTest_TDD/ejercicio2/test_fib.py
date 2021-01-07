from fib import fib

def test_fib1():
    n1 = 2
    n2 = 5
    n3 = 6
    n4 = 11
    fib_12 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 24, 55, 89]
    
    assert fib(n1) == fib_12[n1]
    assert fib(n2) == fib_12[n2]
    assert fib(n3) == fib_12[n3]
    assert fib(n4) == fib_12[n4]
