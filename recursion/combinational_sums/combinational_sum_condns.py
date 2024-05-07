def get_combs(idx, arr, target, lst, ans):
    if idx == len(arr):
        if target == 0:
            ans.append(list(lst))
        return

    if target == 0:
        ans.append(list(lst))
        return
    for i in range(idx, len(arr)):
        if i > idx and arr[i] == arr[i - 1]:
            continue
        if arr[i] > target:
            break
        lst.append(arr[i])
        get_combs(i + 1, arr, target - arr[i], lst, ans)
        lst.pop()


ans = []
lst = []
arr = [10, 1, 2, 7, 6, 1, 5]
arr.sort()
target = 8
get_combs(0, arr, target, lst, ans)
print(ans)
