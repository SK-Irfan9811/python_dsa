def reverse_array(arr, l, r):
    if r <= l:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    return reverse_array(arr, l + 1, r - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse_array(arr, 0, len(arr)-1))
