def f(g):
    a = 2
    return lambda y: a * g(y)


a = 1
print(f(lambda y : a + y)(a))