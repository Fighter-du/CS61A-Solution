def num_eights(n):
    """ Return the number of times 8 appears as a digit of n.
    >>>num_eights(18)
    1
    >>>num_eights(88)
    2
    >>>num_eights(3)
    0
    :param n:
    :return:
    """
    if n < 10 and n == 8:
        return 1
    elif n < 10 and not n == 8:
        return 0
    curr_digit = n % 10
    if curr_digit == 8:
        return 1 + num_eights(n // 10)
    else:
        return num_eights(n // 10)