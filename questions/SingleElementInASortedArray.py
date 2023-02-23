from typing import List


class Solution:

    def single_non_duplicate(self, nums: List[int]) -> int:

        start = 0
        end = len(nums)-1

        while start < end:
            mid = (start + end)//2

            if mid % 2:
                if nums[mid] == nums[mid+1]:
                    end = mid-1
                else:
                    start = mid + 1
            else:
                if nums[mid] == nums[mid+1]:
                    start = mid+1
                else:
                    end = mid

        return nums[end]


def test():
    assert Solution().single_non_duplicate([1, 1, 2, 2, 4, 5, 5, 6, 6]) == 4
    assert Solution().single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert Solution().single_non_duplicate([3, 3, 7, 7, 10, 11, 11]) == 10
    assert Solution().single_non_duplicate([3, 3, 11]) == 11
    assert Solution().single_non_duplicate([3, 11, 11]) == 3