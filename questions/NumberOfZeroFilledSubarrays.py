from typing import List


class Solution:
    def zero_filled_subarray(self, nums: List[int]) -> int:
        result = 0
        current_count = 0
        zero_chain = 0

        for val in nums:

            if val == 0:
                zero_chain += 1
                current_count = current_count + zero_chain
            else:
                result += current_count
                zero_chain = 0
                current_count = 0

        if current_count != 0:
            result += current_count

        return result


def test():
    assert Solution().zero_filled_subarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert Solution().zero_filled_subarray([0, 0, 0, 1, 0]) == 7
