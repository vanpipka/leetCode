from typing import List


class Solution:
    def pivot_index(self, nums: List[int]) -> List[int]:

        nums_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == nums_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1


def test():
    assert Solution().pivot_index([-1, -1, 0, 1, 1, 1]) == 5
    assert Solution().pivot_index([-1, -1, 0, 1, 1, 0]) == 5
    #assert Solution().pivot_index([1, 7, 3, 6, 5, 6]) == 3
    #assert Solution().pivot_index([1, 2, 3]) == -1
    #assert Solution().pivot_index([2, 1, -1]) == 0
