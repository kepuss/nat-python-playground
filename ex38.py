input_list = [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]


def check_sum_of_list_elements(input):
    return sum(input) == 0


def check_sum_of_nested_list_elements(nested_list):
    result = []
    for element in nested_list:
        result.append(check_sum_of_list_elements(element))
    return result

print(check_sum_of_nested_list_elements(input_list))