import py
import pytest

from numbers_to_dec import list_to_decimal

def test_wrong_input_type():
    with pytest.raises(TypeError):
        list_to_decimal(['word'])

    with pytest.raises(TypeError):
        list_to_decimal([3.81])

def test_empty_list():
    with pytest.raises(ValueError):
        list_to_decimal([])

def test_num_out_of_range():
    with pytest.raises(ValueError):
        list_to_decimal([0, 11])

    with pytest.raises(ValueError):
        list_to_decimal([-1, 10])

    with pytest.raises(ValueError):
        list_to_decimal([-0, -10])

def test_starts_with_zero():
    with pytest.raises(ValueError):
        list_to_decimal([0, 10])

def test_return_type():
    isinstance(list_to_decimal([2, 3]), int)

def test_correct_output():
    list_to_decimal([1, 7, 5]) == 175
    list_to_decimal([0,3,1,2]) == 312
