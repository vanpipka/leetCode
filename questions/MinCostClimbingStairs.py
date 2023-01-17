from typing import List
import math


class Solution:

    def min_cost_climbing_stairs(self, cost: str) -> List[str]:

        if not cost:
            return 0

        cur = 0
        dp0 = cost[0]
        dp1 = 0

        if len(cost) >= 2:
            dp1 = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cur

        return min(dp0, dp1)


def test():
    assert Solution().min_cost_climbing_stairs([15, 1, 5]) == 1
    assert Solution().min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6