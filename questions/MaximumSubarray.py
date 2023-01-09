from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:

        result = float('-inf')
        curr = 0

        for i in nums:
            curr += i
            if curr > result:
                result = curr
            if curr < 0:
                curr = 0

        return result


def test():
    #assert Solution().max_sub_array([1,2,-1,-2,2,1,-2,1,4,-5,4]) == 6
    assert Solution().max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
