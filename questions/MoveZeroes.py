from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        i = len(nums)
        while i > 0:
            i -= 1
            if nums[i-1] == 0:
                nums.append(0)
                nums.pop(i-1)

        return nums
