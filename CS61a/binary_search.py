def binary_search(lst, l, r, target):
    mid = int((l+r)/2)
    if l == r:
        if lst[mid] == target:
            return mid
        else:
            return None
    if lst[mid] > target:
        return binary_search(lst, l, mid, target)
    else:
        return binary_search(lst, mid+1, r, target)


print(binary_search([1, 2, 3, 4, 5], 0, 4, 9))