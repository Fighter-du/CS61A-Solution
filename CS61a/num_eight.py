def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.
    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    if n%10 == 8:
        return 1+num_eights(int(n/10))
    else:
        return num_eights(int(n/10))
