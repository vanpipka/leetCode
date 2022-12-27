from typing import List


# need to use binary search (for example) for better performance
class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:

        result = 0

        for i in range(len(nums)):
            if nums[i] >= target:
                return result
            result += 1

        return result
