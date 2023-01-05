from typing import List


class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:

        return sorted([i**2 for i in nums])


def test():
    assert Solution().sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution().sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]


