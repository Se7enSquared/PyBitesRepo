from fibonacci import fib
import pytest
# write one or more pytest functions below, they need to start with test_
def test_n_less_than_zero():
    with pytest.raises(ValueError):
        fib(-1)

def test_n_0_1():
    assert(fib(0), 0)
    assert(fib(1), 1)

def test_fib():
    assert(fib(3), [1,1,2,3])
    assert(fib(13), [1,1,2,3,5,8,13])