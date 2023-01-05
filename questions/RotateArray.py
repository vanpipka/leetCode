from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:

        for i in range(k):
            nums.insert(0, nums.pop())

        return nums


def test():
    assert Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert Solution().rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
