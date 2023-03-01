from typing import List


class Solution:

    def search_max(self, nums: List[int], target: int) -> int:

        _max = -1
        start, end = 0, len(nums) - 1
        mid = 0

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    _max = max(_max, mid)
                start = mid+1
            else:
                end = mid - 1

        return _max

    def search_min(self, nums: List[int], target: int) -> int:

        _min = float("inf")
        start, end = 0, len(nums)-1
        mid = 0

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    _min = min(_min, mid)
                end = mid - 1
            else:
                start = mid + 1

        if _min == float("inf"):
            return - 1

        return _min

    def search_range(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        _min = self.search_min(nums, target)
        _max = self.search_max(nums, target)

        print([_min, _max])

        return [_min, _max]


def test():
    assert Solution().search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().search_range([2, 2], 2) == [0, 1]
