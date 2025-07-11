def divide(quotients, divisors):
    """
    It returns a dictionary whose key q is element of QUOTIENTS and whose values are elements in divisors that can be divided by q
    :param quotients:
    :param divisors:
    :return:
    >>> divide([3, 4, 5], [8, 9, 10, 11, 12])
    {3: [9, 12], 4: [8, 12], 5: [10]}
    >>> divide(range(1, 5), range(20, 25))
    {1: [20, 21, 22, 23, 24], 2: [20, 22, 24], 3: [21, 24], 4: [20, 24]}
    """
    result_dict = {}
    for q in quotients:
        values_lst = []
        for divisor in divisors:
            if divisor % q == 0:
                values_lst.append(divisor)
        result_dict[q] = values_lst
    return result_dict