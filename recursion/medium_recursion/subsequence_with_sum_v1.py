def get_subsequences_with_sum(arr, idx, K, lst):
    if idx == len(arr):
        if sum(lst) == K:
            print(lst)
        return

    lst.append(arr[idx])
    get_subsequences_with_sum(arr, idx + 1, K, lst)
    lst.remove(arr[idx])
    get_subsequences_with_sum(arr, idx + 1, K, lst)


arr = [1, 2, 3, 4, 5]
K = 5
S = 0
lst = []
get_subsequences_with_sum(arr, 0, K, lst)
