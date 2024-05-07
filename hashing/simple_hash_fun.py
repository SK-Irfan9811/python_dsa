arr = [int(x) for x in input().split(",")]
# the motto is to count the frequency of elements in the array
hash_arr = [0] * len(arr)

for i in arr:
    hash_arr[i] += 1
for i in list(set(arr)):
    print(i, "'s frequency is ", hash_arr[i])
