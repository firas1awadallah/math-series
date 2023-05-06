import pytest
from series import fibonacci
from series import lucas
from series import sum_series

# test fibonacci
def test_fibonacci_0() :
    actual = fibonacci(0)
    excepted = 0
    assert actual == excepted

def test_fibonacci_1() :
    actual = fibonacci(1)
    excepted = 1
    assert actual == excepted

def test_fibonacci_2() :
    actual = fibonacci(2)
    excepted = 1
    assert actual == excepted

def test_fibonacci_3() :
    actual = fibonacci(3)
    excepted = 2
    assert actual == excepted

def test_fibonacci_4() :
    actual = fibonacci(4)
    excepted = 3
    assert actual == excepted

def test_fibonacci_5() :
    actual = fibonacci(5)
    excepted = 5
    assert actual == excepted

def test_fibonacci_6() :
    actual = fibonacci(6)
    excepted = 8
    assert actual == excepted

# test lucas
def test_lucas_0() :
    actual = lucas(0)
    excepted = 2
    assert actual == excepted

def test_lucas_1() :
    actual = lucas(1)
    excepted = 1
    assert actual == excepted

def test_lucas_2() :
    actual = lucas(2)
    excepted = 3
    assert actual == excepted

def test_lucas_3() :
    actual = lucas(3)
    excepted = 4
    assert actual == excepted

def test_lucas_4() :
    actual = lucas(4)
    excepted = 7
    assert actual == excepted

def test_lucas_5() :
    actual = lucas(5)
    excepted = 11
    assert actual == excepted

def test_lucas_6() :
    actual = lucas(6)
    excepted = 18
    assert actual == excepted

# test as fibonacci
def test_sum_series_7() :
    actual = sum_series(7)
    excepted = 13
    assert actual == excepted   

def test_sum_series_8() :
    actual = sum_series(8)
    excepted = 21
    assert actual == excepted 

def test_sum_series_9() :
    actual = sum_series(9)
    excepted = 34
    assert actual == excepted    

def test_sum_series_10() :
    actual = sum_series(10)
    excepted = 55
    assert actual == excepted 

# test as lucas
def test_sum_series_7_2_1() :
    actual = sum_series(7 , 2 , 1)
    excepted = 29
    assert actual == excepted 

def test_sum_series_8_2_1() :
    actual = sum_series(8 , 2 , 1)
    excepted = 47
    assert actual == excepted 

def test_sum_series_9_2_1() :
    actual = sum_series(9 , 2 , 1)
    excepted = 76
    assert actual == excepted 

def test_sum_series_10_2_1() :
    actual = sum_series(10 , 2 , 1)
    excepted = 123
    assert actual == excepted     

# Test a custom series
    
def test_sum_series_0_3_2() :
    actual = sum_series(0, 3, 2)
    excepted = 3
    assert actual == excepted    

def test_sum_series_3_3_2() :
    actual = sum_series(3, 3, 2)
    excepted = 7
    assert actual == excepted   

def test_sum_series_5_3_2() :
    actual = sum_series(5, 3, 2)
    excepted = 19
    assert actual == excepted  
