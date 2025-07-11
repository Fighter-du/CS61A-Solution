def divisible_by_k(n, k):
    facts = []
    size = 0
    for i in range(1, n + 1):
        if i % k == 0:
            facts.append(i)
            size += 1
    return facts, size
