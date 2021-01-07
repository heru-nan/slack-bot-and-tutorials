
from primes import is_prime

def test_prime_number():
    assert is_prime(1) == False

def test_prime_number_2():
    assert is_prime(29) == True

def test_prime_number_3():
    assert is_prime(24) == False
