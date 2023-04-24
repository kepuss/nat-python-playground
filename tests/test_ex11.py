from ex_solutions.ex11 import find_indexes_below_threshold
import pytest


def test_find_indexes_below_threshold_positive():
    input_list = [12, 0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
    threshold = 100
    assert find_indexes_below_threshold(input_list, threshold) == [
        0, 1, 2, 3, 4, 8, 9, 10, 11]


def test_find_indexes_below_threshold_empty_list():
    input_list = [12, 0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
    threshold = 0
    assert find_indexes_below_threshold(input_list, threshold) == []


def test_check_if_list_elements_differ_by_10_raises_ValueError_for_negative_value():
    with pytest.raises(ValueError):
        input_list = [12, 0, 12, 45, 3, -4923, 322, 105, 29, 15, 39, 55]
        threshold = 100
        find_indexes_below_threshold(input_list, threshold)


def test_check_if_list_elements_differ_by_10_raises_TypeError_for_nonintegers():
    with pytest.raises(TypeError):
        input_list = [12, 0, 12, 45, 3, 4923, 322, 105, '29', 15, 39, 55]
        threshold = 100
        find_indexes_below_threshold(input_list, threshold)
