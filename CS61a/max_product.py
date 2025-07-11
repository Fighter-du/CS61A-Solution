def max_product(s):
    """
    返回s的最大非连续积
    :param s:
    :return:
    >>> max_product([1, 2, 3, 4]) # 2 * 4
    8
    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    """
    if len(s) == 1:
        return s[0]
    if len(s) == 2:
        return max(s[0], s[1])
    return max(s[0] * max_product(s[2:]), max_product(s[1:]))
