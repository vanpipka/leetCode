from typing import List


# need to use binary search (for example) for better performance
class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:

        result = 0

        for i in range(len(nums)):
            if nums[i] >= target:
                return result
            result += 1

        return result


def test():
    assert Solution().search_insert(nums=[1, 3, 5, 6], target=5) == 2
    assert Solution().search_insert(nums=[1, 3, 5, 6], target=2) == 1
    assert Solution().search_insert(nums=[1, 3, 5, 6], target=7) == 4
