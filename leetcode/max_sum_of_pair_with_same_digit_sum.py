from collections import defaultdict
from sortedcontainers import SortedSet

nums = [18,43,36,13,7]
sum_map = defaultdict(int)
ele_map = {}


def digit_sum(num):
    return sum(list(int(x) for x in str(num)))


sum_ = -1
for item in nums:
    item_sum = digit_sum(item)
    if item_sum in sum_map:
        if sum_ < item + ele_map[item_sum]:
            sum_ = item + ele_map[item_sum]
        ele_map[item_sum] = max(item, ele_map[item_sum])

    sum_map[item_sum] += 1
    ele_map[item_sum] = item
print(sum_, ele_map, sum_map)
