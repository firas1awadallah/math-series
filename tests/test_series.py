import pytest
from series import fibonacci
from series import lucas
from series import sum_series
def test_fibonacci() :
    actual = fibonacci(3)
    excepted = 2
    assert actual == excepted

def test_lucas() :
    actual = lucas(6)
    excepted = 18
    assert actual == excepted

def test_sum_series() :
    actual = sum_series(4, 3, 4)
    excepted = 18
    assert actual == excepted    
