from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:

        result = 0

        for i in nums:
            result = result ^ i

        return result


def test():
    assert Solution().single_number([4, 1, 2, 1, 2]) == 4
    assert Solution().single_number([2, 1, 2]) == 1
