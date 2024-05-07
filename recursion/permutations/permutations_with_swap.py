def get_permutations(arr, idx):
    if idx == len(arr):
        print(arr)
        return
    for i in range(idx, len(arr)):
        arr[i], arr[idx] = arr[idx], arr[i]
        get_permutations(arr, idx + 1)
        arr[i], arr[idx] = arr[idx], arr[i]


get_permutations([1, 2, 3], 0)
