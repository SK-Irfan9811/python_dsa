def print_permu(idx, arr):
    if idx == len(arr) - 1:
        print(arr)
        return
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        print_permu(idx + 1, arr)
        arr[idx], arr[i] = arr[i], arr[idx]


arr = [1, 2, 3]
print_permu(0, arr)
