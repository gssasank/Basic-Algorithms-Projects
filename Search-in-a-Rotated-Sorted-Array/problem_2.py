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
    pivot_index = find_pivot_element(input_list, first, last)

    if pivot_index == -1:
        return binary_search(input_list, first, last, number)
    else:
        if input_list[pivot_index] == number:
            return pivot_index
        elif number >= input_list[0]:
            return binary_search(input_list, 0, pivot_index - 1, number)

        return binary_search(input_list, pivot_index + 1, last, number)


def find_pivot_element(array, min, max):
    if max < min:
        return -1

    if max == min:
        return max

    else:
        key = (min + max) // 2

        if key < max and array[key] > array[key + 1]:
            return key

        if key > min and array[key - 1] > array[key]:
            return key - 1

        if array[min] >= array[key]:
            return find_pivot_element(array, min, key - 1)

        return find_pivot_element(array, key + 1, max)


# Used Recursive Binary Search
def binary_search(array, low, high, target):
    if low > high:
        return -1

    key = (low + high) // 2
    if array[key] == target:
        return key
    elif array[key] > target:
        return binary_search(array, low, key - 1, target)
    elif array[key] < target:
        return binary_search(array, key + 1, high, target)


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
