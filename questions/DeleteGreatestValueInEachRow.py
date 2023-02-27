from typing import List


class Solution:
    def delete_greatest_value(self, grid: List[List[int]]) -> int:

        for i in grid:
            i.sort()
        result = 0
        for i in range(len(grid[0])):
            _max = 0
            for x in range(len(grid)):
                _max = max(_max, grid[x][i])
            result += _max
        return result


def test():
    assert Solution().delete_greatest_value([[1, 2, 4], [3, 3, 1]]) == 8



