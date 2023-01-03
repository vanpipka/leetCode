from typing import List


class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:

        return sorted([i**2 for i in nums])


