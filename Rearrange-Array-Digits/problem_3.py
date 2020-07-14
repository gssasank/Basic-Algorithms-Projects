def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = merge_sort(input_list)
    num_1 = "0"
    num_2 = "0"
    index = len(sorted_list) - 1
    while index >= 0:
        if index % 2 == 0:
            num_1 += str(sorted_list[index])
        else:
            num_2 += str(sorted_list[index])

        index -= 1

    if int(num_1) > int(num_2):
        return int(num_1), int(num_2)
    else:
        return int(num_2), int(num_1)


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_1)
test_case_2 = [[0, 0, 0, 0, 0, 0, 0], [0, 0]]
test_function(test_case_2)
test_case_3 = [[9, 8, 7, 6, 5, 4, 3, 2, 1], [97531, 8642]]
test_function(test_case_3)
# edge case : single value list
test_function([[5], [5, 0]])

# edge case 2: large set and large numbers
test_function([[i for i in range(0, 101)],
               [int("".join(map(str, range(100, -1, -2)))), int("".join(map(str, range(99, -1, -2))))]])
