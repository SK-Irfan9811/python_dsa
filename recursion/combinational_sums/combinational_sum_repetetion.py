def get_combination_sum(idx, arr, target, ds, ans):
    if target == 0:
        ans.append(list(ds))
        return

    if idx == len(arr):
        if target == 0:
            ans.append(list(ds))
        return
    if arr[idx] <= target:
        ds.append(arr[idx])
        get_combination_sum(idx, arr, target - arr[idx], ds, ans)
        ds.pop()
    get_combination_sum(idx + 1, arr, target, ds, ans)


ds = []
ans = []
get_combination_sum(0, [1, 2, 3, 4, 5], 7, ds, ans)
print(ans)
