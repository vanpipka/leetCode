from collections import defaultdict
from typing import List


class Solution:
    def four_sum_count(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        nums_len = len(nums)
        result = []

        for x in range(nums_len-3):
            for y in range(x+1, nums_len - 2):
                sum = nums[x]+nums[y]
                i, j = y+1, nums_len-1
                while i < j:
                    if sum + nums[i] + nums[j] == target:
                        lst = sorted([nums[x], nums[y], nums[i], nums[j]])
                        if lst not in result:
                            result.append(lst)
                        i += 1
                        j -= 1
                    elif sum + nums[i] + nums[j] < target:
                        i += 1
                    else:
                        j -= 1

        print(result)
        return result


def test():

    assert Solution().four_sum_count([-3, -2, -1, 0, 0, 1, 2, 3], 0) == []
    assert Solution().four_sum_count([2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert Solution().four_sum_count([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
