from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        x, y = 0, len(nums)-1

        while x <= y:

            mid = (x+y)//2
            if nums[mid] == target:
                return mid

            if nums[x] <= nums[mid]:  # отсортированный кусок слева
                if nums[x] <= target < nums[mid]:
                    y = mid - 1
                else:
                    x = mid + 1
            else:
                if nums[mid] < target <= nums[y]:
                    x = mid + 1
                else:
                    y = mid - 1

        return -1


def test():
    assert Solution().search([3, 1], 1) == 1
    assert Solution().search([7, 0, 2, 3, 4, 5, 6], 7) == 0
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution().search([4, 5, 6, 7, 0, 3, 2], 3) == 5
