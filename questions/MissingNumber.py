from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:

        nums = sorted(nums)

        if nums[0] != 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                return nums[i-1]+1

        return nums[-1]+1


def test():
    assert Solution().missing_number([1]) == 0
    assert Solution().missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert Solution().missing_number([0, 1]) == 2


