def interleaved_sum(n, odd_func, even_func):
    """Compute the odd_func(1) + even_func(2) + odd_func(3) + to the n.
    :param n:
    :param odd_func:
    :param even_func:
    :return:
    """
    def odd_helper(i):
        if i > n:
            return 0
        return odd_func(i) + even_helper(i + 1)

    def even_helper(i):
        if i > n:
            return 0
        return even_func(i) + odd_helper(i + 1)

    return odd_helper(1)

