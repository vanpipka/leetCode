from typing import List


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:

        result = [nums[0]]

        for i in range(1, len(nums)):
            result.append(result[-1]+nums[i])

        print(result)

        return result


def test():
    assert Solution().running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert Solution().running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
