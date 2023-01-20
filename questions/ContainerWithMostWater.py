from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:

        result = 0
        left, right = 0, len(height)-1

        while True:
            if left == right:
                break

            dist = right-left

            if height[left] < height[right]:
                result = max(result, height[left] * dist)
                left += 1
            else:
                result = max(result, height[right] * dist)
                right -= 1

        return result


def test():
    assert Solution().max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
