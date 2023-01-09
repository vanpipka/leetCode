from typing import List


class Solution:
    def contains_dublicate(self, nums: List[int]) -> int:

        return len(set(nums)) != len(nums)

def test():
    assert Solution().contains_dublicate([1, 2, 3, 1]) is True
    assert Solution().contains_dublicate([1, 2, 3, 4]) is False
    assert Solution().contains_dublicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
