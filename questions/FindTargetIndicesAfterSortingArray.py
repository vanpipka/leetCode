from typing import List


class Solution:
    def target_indices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()

        result = []
        for i, val in enumerate(nums):
            if val == target:
                result.append(i)

        return result


def test():
    assert Solution().target_indices([1, 2, 5, 2, 3], 2) == [1, 2]
