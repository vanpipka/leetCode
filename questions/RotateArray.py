from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:

        for i in range(k):
            nums.insert(0, nums.pop())

        return nums
