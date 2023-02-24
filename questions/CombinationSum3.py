from typing import List


class Solution:
    def combination_sum3(self, k: int, n: int) -> List[List[int]]:

        candidates = [i for i in range(1, 10)]
        result = []

        def dfs(lst, _candidates, summ):

            lst_len = len(lst)

            if summ == n and lst_len == k:
                result.append(lst.copy())
                return

            if summ > n or lst_len >= k:
                return

            for i in range(len(_candidates)):
                lst.append(_candidates[i])
                dfs(lst, _candidates[i+1:], summ+_candidates[i])
                lst.pop()

        dfs([], candidates, 0)

        print(result)

        return result


def test():
    assert Solution().combination_sum3(3, 7) == [[1, 2, 4]]

