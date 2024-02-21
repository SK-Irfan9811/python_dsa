# finding a majority element in an array which appears n/2 times(n->array size)
def get_max_rep_ele(arr):
    max_ele = arr[0]
    cnt = 0
    for i in arr[1:]:
        if cnt == 0:
            max_ele = i
        elif i == max_ele:
            cnt += 1
        else:
            cnt -= 1

    return max_ele


print(get_max_rep_ele([3, 2, 3]))
print(get_max_rep_ele([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]))
