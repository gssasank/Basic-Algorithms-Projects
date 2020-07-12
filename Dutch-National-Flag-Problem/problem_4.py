def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    ones_array = []
    twos_array = []
    zeroes_array = []
    for number in input_list:

        if number == 0:
            zeroes_array.append(number)
        elif number == 1:
            ones_array.append(number)
        elif number == 2:
            twos_array.append(number)
    return zeroes_array + ones_array + twos_array


def test_function(test_case):
    if not len(test_case):
        print("Pass")
        return
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
