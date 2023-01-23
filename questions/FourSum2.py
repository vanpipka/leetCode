from collections import defaultdict
from typing import List


class Solution:
    def four_sum_count(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        sums, res = {}, 0

        for x in nums1:
            for y in nums2:
                tmp = x+y
                sums[tmp] = sums.get(tmp, 0) + 1

        for i in nums3:
            for j in nums4:
                tmp = -(i + j)
                res += sums.get(tmp, 0)

        return res


def test():

    assert Solution().four_sum_count(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]) == 2