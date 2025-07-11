def sum_digits(n):
    sum = 0
    while n:
        last_digit = n % 10
        sum += last_digit
        n //= 10
    return sum
