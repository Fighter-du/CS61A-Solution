def sums(n, m):
    """
    返回总和为n，最大值为m的所有一维列表组成的二维列表
    :param n:
    :param m:
    :return:
    """
    return [[m] + sums(n - m, m)] + sums(n, m - 1)
