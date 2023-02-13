import math
from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.result = 0

    def minimum_fuel_cost(self, roads: List[List[int]], seats: int) -> int:

        paths = defaultdict(set)
        visited = {0}
        for a, b in roads:
            paths[a].add(b)
            paths[b].add(a)

        def dfs(value: int):

            reps = 1
            node = paths.get(value)
            if not node:
                return reps

            for i in node:
                if i not in visited:
                    visited.add(i)
                    reps += dfs(i)

            if value != 0:
                self.result += math.ceil(reps / seats)

            return reps

        dfs(0)

        return self.result


def test():
    assert Solution().minimum_fuel_cost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2) == 7
    assert Solution().minimum_fuel_cost([[0, 1], [0, 2], [0, 3]], 5) == 3
