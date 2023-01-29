from typing import List


class Solution:
    # Using Kadane's algorithm
    def max_product(self, nums: List[int]) -> int:

        print("----------------")

        if len(nums) == 0:
            return 0

        _max, _min = nums[0], nums[0]
        result = _max

        for i in range(1, len(nums)):

            current = nums[i]
            _max_temp = max(current, _max * current, current * _min)
            _min = min(current, _max * current, current * _min)
            _max = _max_temp

            print(f"min: {_min} | max: {_max}")

            result = max(result, _max)

        return result


def test():
    assert Solution().max_product([1, 3, 3, -1, 4, -3, -1, 6, 1]) == 108
    assert Solution().max_product([2, 3, -2, 4]) == 6
