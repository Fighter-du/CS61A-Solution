def close(s, k):
    count = 0
    for i in range(len(s)):
        if abs(s[i] - i) <= k:
            count += 1
    return count
