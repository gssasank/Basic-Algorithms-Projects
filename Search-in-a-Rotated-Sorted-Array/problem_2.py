def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    first_element = find_first_element(input_list)
    if first_element == input_list[0]:
        return binary_search(input_list, number)
    elif input_list[first_element] == number:
        return first_element


def find_first_element(input_list):
    min = input_list[0]
    for i in input_list:
        if i < min:
            min = i
    return min


def binary_search(array, target):
    first_element = 0
    last_element = len(array) - 1
    while first_element <= last_element:
        key = (first_element + last_element) // 2
        if array[key] == target:
            return key
        else:
            if target > array[key]:
                first_element = key
            elif target < array[key]:
                last_element = key


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if binary_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
