from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        twoBack = 0
        oneBack = nums[0]
        for n in range(1, len(nums)):
            temp = oneBack
            oneBack = max(oneBack, nums[n] + twoBack)
            twoBack = temp

        return oneBack

def test():

    #assert Solution().rob([1, 2, 3, 1]) == 4
    #assert Solution().rob([1, 2]) == 2
    #assert Solution().rob([2, 1, 1, 2]) == 4
    assert Solution().rob([2, 3, 1, 14, 15, 2]) == 19
