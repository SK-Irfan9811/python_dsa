from collections import defaultdict

nums = [3, 2, 5, 6, 4, 8]
n = len(nums)
good_pairs = 0
freq = defaultdict(int)
# find no.of good pairs
for i in range(n):
    diff = nums[i] - i
    if diff in freq:
        good_pairs += freq[diff]
    freq[diff] += 1

print(good_pairs)
print(n * (n - 1) // 2 - good_pairs)
