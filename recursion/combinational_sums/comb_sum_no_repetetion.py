def get_combination_sum(idx, arr, target, ds, ans):
    if idx == len(arr):
        if target == 0:
            ans.add(tuple(sorted(list(ds))))
        return
    ds.append(arr[idx])
    get_combination_sum(idx + 1, arr, target - arr[idx], ds, ans)
    ds.pop()
    get_combination_sum(idx + 1, arr, target, ds, ans)


ans = set()
lst = []
get_combination_sum(0, [10,1,2,7,6,1,5], 8, lst, ans)
print(ans)
