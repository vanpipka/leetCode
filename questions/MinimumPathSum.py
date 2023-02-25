from typing import List


class Solution:
    def min_path_sum(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            for x in range(len(grid[i])):

                if i == 0 and x == 0:
                    continue
                if i == 0:
                    grid[i][x] += grid[i][x-1]
                    continue
                if x == 0:
                    grid[i][x] += grid[i-1][x]
                    continue
                grid[i][x] += min(grid[i-1][x], grid[i][x-1])

        return grid[-1][-1]


def test():
    assert Solution().min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
