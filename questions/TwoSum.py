from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:

        res = []

        for i_y, y in enumerate(nums):

            try:

                i_x = nums.index(target - y, i_y + 1)
                res.append(i_y)
                res.append(i_x)

                break

            except ValueError:

                continue

        return res


def test():
    assert Solution().two_sum([2, 7, 11, 15], 9) == [0, 1]

