def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       number:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0 or number is None:
        return -1

    first = 0
    last = len(input_list) - 1
    try:
        max_element_index = input_list.index(max(input_list))
    except KeyError:
        return -1

    if max_element_index == -1:
        return binary_search(input_list, first, last, number)
    else:
        if input_list[max_element_index] == number:
            return max_element_index
        elif number >= input_list[0]:
            return binary_search(input_list, 0, max_element_index, number)
        else:
            return binary_search(input_list, max_element_index, last, number)


# Used Recursive Binary Search
def binary_search(array, start_index, end_index, target):

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_element = array[mid_index]

        if target == mid_element:
            return mid_index

        elif target < mid_element:
            end_index = mid_index - 1

        else:
            start_index = mid_index + 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[0], 0])
test_function([[0, 0, 0, 0, 0, 0, 0], 0])

# edge test 1  empty string
test_function([[], 1])
# edge test 2  large list
test_list = [i for i in range(1011, 10000)] + [i for i in range(0, 1011)]
test_function([test_list, 6])
# edge test 3  large list with negative numbers
test_list = [i for i in range(1011, 10000)] + [i for i in range(-1000, 1011)]
test_function([test_list, -60])
