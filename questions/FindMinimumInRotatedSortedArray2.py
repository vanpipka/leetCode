from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:

        x, y = 0, len(nums)-1

        target = float("inf")

        while x <= y:

            mid = (x+y)//2

            target = min(nums[mid], target)

            if nums[mid] == nums[y]:
                if nums[mid] == nums[x]:
                    x += 1
                elif nums[x] < nums[mid]:
                    y = mid - 1
                else:
                    y = mid
            elif nums[y] < nums[mid]:
                x = mid + 1
            else:
                y = mid - 1

        return target


def test():
    assert Solution().find_min([1, 3, 3]) == 1
    assert Solution().find_min([3, 3, 1, 3]) == 1
    assert Solution().find_min([2, 2, 2, 0, 1]) == 0
    assert Solution().find_min([1, 3, 5]) == 1
    assert Solution().find_min([3, 1]) == 1
    assert Solution().find_min([7, 0, 2, 3, 4, 5, 6]) == 0
    assert Solution().find_min([4, 5, 6, 7, 9, 1, 4]) == 1
    assert Solution().find_min([4, 5, 6, 7, 0, 1, 2]) == 0
