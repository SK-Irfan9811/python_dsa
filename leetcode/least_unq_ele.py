from collections import Counter
from typing import List


def find_least_num_of_unique_ints(self, arr: List[int], k: int) -> int:
    if k == 0:
        return len(set(arr))

    freq_map = Counter(arr)
    l = len(freq_map)
    d = 0
    sorted_map = sorted(freq_map.items(), key=lambda x: x[1])
    for i in sorted_map:
        if k >= i[1]:
            k -= i[1]
            d += 1
        else:
            break

    return l - d
