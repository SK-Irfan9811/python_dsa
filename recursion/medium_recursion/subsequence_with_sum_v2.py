def get_subsequences_with_sum(arr, idx, K, lst):
    if idx == len(arr):
        if sum(lst) == K:
            print(lst)
            return True
        return False

    lst.append(arr[idx])
    if get_subsequences_with_sum(arr, idx + 1, K, lst):
        return True
    lst.remove(arr[idx])
    if get_subsequences_with_sum(arr, idx + 1, K, lst):
        return True
    return False


arr = [1, 2, 3, 4, 5]
K = 5
S = 0
lst = []
print(get_subsequences_with_sum(arr, 0, K, lst))
