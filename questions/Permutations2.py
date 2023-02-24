from typing import List


class Solution:
    def permute_unique(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums_len = len(nums)

        def dfs(lst, _nums):
            lst_len = len(lst)
            if lst_len == nums_len:
                if lst not in result:
                    result.append(lst.copy())
                return
            if lst_len > nums_len:
                return

            for i in range(len(_nums)):
                lst.append(_nums[i])
                dfs(lst, _nums[:i] + _nums[i + 1:])
                lst.pop()

        dfs([], nums)

        return result


def test():
    assert Solution().permute_unique([1,1,2]) == [[1,1,2],[1,2,1],[2,1,1]]

