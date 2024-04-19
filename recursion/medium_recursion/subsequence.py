def get_subsequences(arr, idx, lst, ds):
    if idx >= len(arr):
        ds.append(list(lst))
        return
    lst.append(arr[idx])
    get_subsequences(arr, idx + 1, lst, ds)
    lst.remove(arr[idx])
    get_subsequences(arr, idx + 1, lst, ds)


arr = [1, 2, 3, 4]  # for n elements we get 2 ** n sub sequences
ds = []
get_subsequences(arr, 0, [], ds)
print(ds)
