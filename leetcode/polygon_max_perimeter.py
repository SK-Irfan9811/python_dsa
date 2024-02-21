from typing import List


def largest_perimeter(self, nums: List[int]) -> int:
    if len(nums) < 3:
        return -1
    nums.sort()
    for i in range(len(nums)):
        temp_lst = nums[0:len(nums) - i - 1]
        summ = sum(temp_lst)
        last_ele = nums[len(nums) - i - 1]
        if len(temp_lst + [last_ele]) < 3:
            return -1
        if summ > last_ele:
            return summ + last_ele
    else:
        return -1
