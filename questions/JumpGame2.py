from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:

        end = len(nums)-1
        result = []

        while end > 0:
            min_i = -1
            for i in reversed(range(end)):

                if nums[i]+i >= end:
                    min_i = i

            result.append(min_i)
            end = min_i

        return len(result)


def test():
    assert Solution().jump([1, 1, 2, 1, 4]) == 3
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([1, 2, 1, 1, 4]) == 3



