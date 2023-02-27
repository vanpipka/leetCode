from typing import List


class Solution:
    def minimum_cost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        result = 0
        for i in range(len(cost)):
            if (i+1) % 3:
                result += cost[i]

        return result


def test():
    assert Solution().minimum_cost([1, 2, 3]) == 5



