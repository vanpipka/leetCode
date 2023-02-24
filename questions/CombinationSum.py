from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(lst, _candidates):

            lst_sum = sum(lst)

            if lst_sum == target:

                comb = lst.copy()
                comb.sort()

                if comb not in result:
                    result.append(comb)
                return

            if lst_sum > target:
                return

            for i in range(len(_candidates)):
                lst.append(_candidates[i])
                dfs(lst, _candidates)
                lst.pop()

        dfs([], candidates)

        print(result)

        return result


def test():
    assert Solution().combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combination_sum([3, 7, 2], 18) == [[3, 3, 3, 3, 3, 3],
                                                         [2, 2, 2, 3, 3, 3, 3],
                                                         [2, 3, 3, 3, 7],
                                                         [2, 2, 2, 2, 2, 2, 3, 3],
                                                         [2, 2, 2, 2, 3, 7],
                                                         [2, 2, 7, 7],
                                                         [2, 2, 2, 2, 2, 2, 2, 2, 2]]
