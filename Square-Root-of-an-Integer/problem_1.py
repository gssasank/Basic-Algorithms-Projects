def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 1:
        return 1
    elif number == 0:
        return 0
    else:
        first = 2
        last = number

        while first <= last:
            middle = (first + last) // 2

            if middle ** 2 == number:
                return middle
            elif middle ** 2 < number:
                first = middle + 1
                answer = middle
            elif middle ** 2 > number:
                last = middle - 1
    return answer


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
