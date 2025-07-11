def is_link(link):
    return link == 'empty' or (len(link) == 2 and is_link(link[1]))


def link(first, rest):
    assert is_link(rest), 'rest必须是一个链表'
    return [first, rest]


def get_first(link):
    assert is_link(link), '输入必须为链表'
    return link[0]


def get_rest(link):
    assert is_link(link), '输入必须为链表'
    return link[1]


def map(f, s):
    """
    返回s中的每一个元素e 的 f(e) 组成的链表
    :param s:
    :return:
    >>> s = [5, [10, [15, 'empty']]]
    >>> f = lambda x : x * x
    >>> map(f, s)
    [25, [100, [225, 'empty']]]
    """
    if s == 'empty':
        return s
    return link(f(get_first(s)), map(f, get_rest(s)))


s = [5, [10, [15, 'empty']]]
f = lambda x : x * x
map(f, s)