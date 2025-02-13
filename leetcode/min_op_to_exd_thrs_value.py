import heapq
from queue import PriorityQueue

nums = [2, 11, 10, 1, 3]
k = 10
# using priority queue
# pq = PriorityQueue()
# for i in nums:
#     pq.put(i)
# counter = 0
# while True:
#     peak_ele = pq.get()
#     if k <= peak_ele:
#         print(counter)
#         break
#     second_peak_ele = pq.get()
#     pq.put(peak_ele * 2 + second_peak_ele)
#     counter += 1

# using heapq
heapq.heapify(nums)

counter = 0
while k > nums[0]:
    f = heapq.heappop(nums)
    s = heapq.heappop(nums)
    heapq.heappush(nums, f * 2 + s)
    counter += 1
print(counter)
