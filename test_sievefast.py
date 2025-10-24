from sievetools import *
import pytest # need for testing value errors

def test_sieve_fast_interior():
    primes = sieve_fast(55) # hard code 55 as input for sanity check
    true_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53] # hard code known list for comparison
    assert primes == true_primes

def test_sievefast_one():
    output = sieve_fast(1)
    assert output == []

def test_sievefast_less():
    with pytest.raises(ValueError):
        sieve_fast(-10) # testable value for that error