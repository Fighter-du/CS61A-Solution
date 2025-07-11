"""
第一次作业 2025.1.3
"""
arr = []


def two_of_three(num1, num2, num3):
    """
    :param num1: 3
    :param num2: 7
    :param num3: 4
    :return: 9, 16
    """
    arr.append(num1)
    arr.append(num2)
    arr.append(num3)
    arr.sort()
    return arr[0]**2, arr[1]**2








