from typing import List


class Solution:
    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if sum(candidates) < target:
            return []

        if len(set(candidates)) == 1:
            if target % candidates[0]:
                return []
            else:
                return [[candidates[0] for _ in range(target // candidates[0])]]

        candidates.sort()

        candidates_len = len(candidates)
        result = []

        def dfs(index, lst, summ):
            if summ == target:
                comb = lst.copy()
                comb.sort()
                if comb not in result:
                    result.append(comb)
                return
            if summ > target:
                return
            for i in range(index, candidates_len):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                lst.append(candidates[i])
                dfs(i + 1, lst, summ + candidates[i])
                lst.pop()

        dfs(0, [], 0)

        return result


def test():
    assert Solution().combination_sum2([2], 1) == []
    assert Solution().combination_sum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 30) == []
    # assert Solution().combination_sum2([1, 1, 1, 1, 1, 1, 1, 1, 1], 8) == [[1, 1, 1, 1, 1, 1, 1, 1]]

