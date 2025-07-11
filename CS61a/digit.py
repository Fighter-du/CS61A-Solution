def digit(n, k):
    while k:
        n //= 10
        k -= 1
    return n % 10
