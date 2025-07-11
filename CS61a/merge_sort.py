def merge(a, a_first, b, b_first):
    if a_first == len(a):
        return b[b_first:]
    elif b_first == len(b):
        return a[a_first:]
    if a[a_first] < b[b_first]:
        return [a[a_first]] + merge(a, a_first+1, b, b_first)
    else:
        return [b[b_first]] + merge(a, a_first, b, b_first+1)


def merge_sort(a, l, r):
    mid = int((l + r)/ 2)
    if l == r:
        return [a[mid]]
    return merge(merge_sort(a, l, mid), 0, merge_sort(a, mid+1, r), 0)


merge_sort([1,9, 2, 5, 3, 4], 0, 5)
