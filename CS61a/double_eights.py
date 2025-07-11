def double_eights(n):
    while n:
        if n % 100 == 88:
            return True
        n //= 10
    return False
