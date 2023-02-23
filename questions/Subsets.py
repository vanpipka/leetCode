from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        nums_len = len(nums)
        result = []

        def dfs(lst, index):

            result.append(lst.copy())

            for i in range(index, nums_len):
                lst.append(nums[i])
                dfs(lst, i+1)
                lst.pop()

        dfs([], 0)

        return result


def test():
    assert Solution().subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
