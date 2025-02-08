from functools import reduce

nums = [1, 2, 4, 8, 16, 32, 64, 128]

freq = {}
prod_list = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        v = nums[i] * nums[j]
        freq[v] = freq.get(v, 0) + 1
        prod_list.append(v)
print(reduce(lambda acc, d: acc + d * (d - 1), freq.values(), 0))
