def get_subset_sum(arr, idx, lst, ans):
    ans.append(list(lst))
    for i in range(idx, len(arr)):
        if i != idx and arr[i] == arr[i - 1]:
            continue

        lst.append(arr[i])
        get_subset_sum(arr, i + 1, lst, ans)
        lst.remove(arr[i])


arr = [1, 2, 2]
ans = []
lst = []
arr.sort()
get_subset_sum(arr, 0, lst, ans)
print(ans)
