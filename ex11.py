input_list = [12, 0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
threshold = 100


def find_indexes_below_threshold(input_list, threshold):
    index_list = []

    if any(item < 0 for item in input_list):
        raise ValueError("Only positive integers are allowed!")
    if not type(threshold) is int:
        raise TypeError("Only integers are allowed!")
    for count, value in enumerate(input_list):
        if value < threshold:
            index_list.append(count)

    return index_list


try:
    print(find_indexes_below_threshold(input_list, threshold))
except Exception as e:
    print("An error has occurred.", e)
