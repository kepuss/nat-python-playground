input_list = [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]

def check_sum_of_nested_list_elements(input):
    for value in input_list:
        if sum(value) == 0:
            print('True')
        else:
            print('False')

print(check_sum_of_nested_list_elements(input_list))