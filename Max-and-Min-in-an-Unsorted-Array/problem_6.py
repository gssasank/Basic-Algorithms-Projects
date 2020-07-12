def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) > 0:
        maximum = ints[0]
        minimum = ints[0]
        for number in ints:
            if number > maximum:
                maximum = number
            if number < minimum:
                minimum = number

        return minimum, maximum

    else:
        return None, None


# Example Test Case of Ten Integers
import random

test_1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_1)

print("Pass" if ((0, 9) == get_min_max(test_1)) else "Fail")

test_2 = []

print("Pass" if ((None, None) == get_min_max(test_2)) else "Fail")

test_3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print("Pass" if ((1, 1) == get_min_max(test_3)) else "Fail")

