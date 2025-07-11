def falling_factorial(n, k):
    if k == 0:
        return 1
    i = n-1
    while not k - 1 == 0:
        n *= i
        i -= 1
        k -= 1
    return n
