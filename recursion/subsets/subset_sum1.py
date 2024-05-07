def get_subset_sum(arr, idx, _sum, ans):
    if idx == len(arr):
        ans.append(_sum)
        return

    get_subset_sum(arr, idx + 1, _sum + arr[idx], ans)
    get_subset_sum(arr, idx + 1, _sum, ans)


arr = [5, 2, 1]
ans = []
get_subset_sum(arr, 0, 0, ans)
print(ans)
