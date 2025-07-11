def paths(m, n):
    """
    找到从m * n网格的左下方到右上方的路经数
    :param m:
    :param n:
    :return:
    """
    if m == 1:
        return 1
    if n == 1:
        return 1
    return paths(m-1, n) + paths(m, n-1)