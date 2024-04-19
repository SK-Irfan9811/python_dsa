def get_subsequences_with_sum(arr, idx, K, lst):
    # this condn is considered when we have positive elements
    if sum(lst) > K:
        return 0
    if idx == len(arr):
        if sum(lst) == K:
            return 1
        return 0

    lst.append(arr[idx])
    l = get_subsequences_with_sum(arr, idx + 1, K, lst)
    lst.remove(arr[idx])
    r = get_subsequences_with_sum(arr, idx + 1, K, lst)
    return l + r


arr = [1, 2, 3, 4, 5]
K = 6
S = 0
lst = []
print(get_subsequences_with_sum(arr, 0, K, lst))
