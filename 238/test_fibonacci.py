from fibonacci import fib
import pytest


def test_n_less_than_zero():
    with pytest.raises(ValueError):
        fib(-1)


def test_n_0():
    assert fib(0) == 0


def test_n_1():
    assert fib(1) == 1


def test_fib():
    assert fib(11) == 89