def only_label(t):
    return type(t) is int


def is_tree(t):
    if only_label(t):
        return True
    if len(t) == 2:
        for branch in branches(t):
            if not is_tree(branch):
                return False
        return True


def tree(r, b):
    return [r, b]


def root(t):
    assert is_tree(t), '输入必须为一个树'
    if only_label(t):
        return t
    return t[0]


def branches(t):
    if only_label(t[1]):
        return [t[1]]
    return t[1]


def has_path(t, p):
    """
    返回t中有没有路径p的布尔值
    :param t:
    :return:
    >>> t = tree(5, tree(10, tree(15, 20)))
    >>> p = [15, 20]
    >>> has_path(t, p)
    True
    >>> p1 = [15, 16]
    >>> has_path(t, p1)
    False
    """
    # base case : 叶子是不是和p一样
    if only_label(t):
        if len(p) > 1:
            return False
        else:
            return t == p[0]
    # Recursion 要么从当前树的label开始和p一样，要么从树的branches开始
    if root(t) == p[0]:
        for branch in branches(t):
            if has_path(branch, p[1:]):
                return True
    else:
        for branch in branches(t):
            if has_path(branch, p):
                return True
    return False


def find_path(t, x):
    """
    找到从t的root到节点x的一条path
    :param t:
    :param x:
    :return:
    >>> t = tree(5, tree(10, tree(15, 20)))
    >>> find_path(t, 20)
    [5, 15, 20]
    """
    def find_path_helper(t, x, found):
        """
        找到从t的root到x的一条path，用found存这条路径
        :param t:initial tree
        :param x:target
        :param found: 从root到当前正在检查的路径
        :return:
        """
        found.append(root(t))
        if only_label(t):
            if t == x:
                return found
            else:
                return None
        if root(t) == x:
            return found
        else:
            for branch in branches(t):
                return_value = find_path_helper(branch, x, found)
                if return_value is not None:
                    return return_value
                else:
                    found.pop()

    return find_path_helper(t, x, [])


