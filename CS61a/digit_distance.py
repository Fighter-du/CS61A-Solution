def digit_distance(n):
    """Return the digit distance.
    >>>digit_distance(10)
    1
    >>>digit_distance(19)
    8
    >>>digit_distance(1)
    0
    :param n:
    :return:
    """
    if n < 10:
        return 0
    sub_digit = abs(n % 10 - (n // 10) % 10)
    if n < 100:
        return sub_digit
    return sub_digit + digit_distance(n // 10)
