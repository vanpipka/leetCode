from typing import List


class Solution:
    def array_pair_sum(self, nums: List[int]) -> int:

        nums.sort()

        pointer = 0
        result = 0

        while pointer < len(nums)-1:
            result += min(nums[pointer], nums[pointer+1])
            pointer += 2

        return result


def test():
    assert Solution().array_pair_sum([1, 4, 3, 2]) == 4



