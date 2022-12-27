from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        result = 0

        for i in range(len(nums)):
            if nums[i] >= target:
                return result
            result += 1

        return result
