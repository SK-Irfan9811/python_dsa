def get_permutations(arr, freq, ds):
    if len(ds) == len(arr):
        print(ds)
        return
    for i in range(len(arr)):
        if not freq[i]:
            freq[i] = True
            ds.append(arr[i])
            get_permutations(arr, freq, ds)
            ds.remove(arr[i])
            freq[i] = False


arr = [1, 2, 3, 3]
freq = [False] * len(arr)

get_permutations(arr, freq, [])
