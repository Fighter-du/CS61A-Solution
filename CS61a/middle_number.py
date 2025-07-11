def middle_number(a, b, c):
    total = a + b + c
    maximum = max(a, max(b, c))
    minimum = min(a, min(b, c))
    return total - minimum - maximum