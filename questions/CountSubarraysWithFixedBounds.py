from typing import List


class Solution:
    def count_subarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        n = len(nums)
        lst = [None for i in range(n)]

        j = -1
        prev_min_index = -1
        prev_max_index = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                j = i
            if num == minK:
                prev_min_index = i
            if num == maxK:
                prev_max_index = i

            lst[i] = max(0, min(prev_min_index, prev_max_index) - j)

        return sum(lst)

def test():
    assert Solution().count_subarrays([1, 1, 5], 1, 5) == 2
    assert Solution().count_subarrays([1, 1, 1], 1, 1) == 6
    assert Solution().count_subarrays([3, 1, 5, 2, 7, 5, 3], 1, 5) == 4
    assert Solution().count_subarrays([2, 3, 1, 5, 2, 4, 7, 5, 3], 1, 5) == 9





