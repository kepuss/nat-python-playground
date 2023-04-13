from ex39 import check_sum_of_nested_list_elements
import pytest


def test_check_sum_of_nested_list_elements_all_true():
    input_list = [[1, 2, -3], [-4, 0, 4],
                  [-1, 16, -15], [0, 1, -1], [-2, 50, -48]]
    assert check_sum_of_nested_list_elements(
        input_list) == [True, True, True, True, True]


def test_check_sum_of_nested_list_elements_all_false():
    input_list = [[6, 2, -3], [-4, 0, 5],
                  [-1, 6, -15], [10, 1, -1], [-2, 50, -8]]
    assert check_sum_of_nested_list_elements(
        input_list) == [False, False, False, False, False]


def test_check_sum_of_nested_list_elements_raises_ValueError_with_no_nested_arrays():
    with pytest.raises(ValueError):
        input_list = []
        check_sum_of_nested_list_elements(input_list)


def test_check_sum_of_nested_list_elements_raises_ValueError_when_nested_array_with_2_elements():
    with pytest.raises(ValueError):
        input_list = [[6, 2, -3], [-4, 0, 5],
                      [-1, -15], [10, 1, -1], [-2, 50, -8]]
        check_sum_of_nested_list_elements(input_list)


def test_check_sum_of_nested_list_elements_raises_ValueError_when_nested_array_with_4_elements():
    with pytest.raises(ValueError):
        input_list = [[6, 2, -3], [-4, 0, 5],
                      [-1, -15], [10, 1, -1], [-2, 50, -8, 99]]
        check_sum_of_nested_list_elements(input_list)
