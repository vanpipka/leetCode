from typing import List


class Solution:

    def __init__(self):
        self.h = 0
        self.w = 0
        self.grid = []
        self.max_area = 0
        self.curr_area = 0
        self.pointer = 0

    def check_point(self, x, y):

        def its_one(x_, y_):
            return self.grid[x_][y_] == 1

        if self.grid[x][y] == 1:
            self.curr_area += 1
            self.grid[x][y] = 2
            if x >= 1:
                if its_one(x - 1, y):
                    self.check_point(x - 1, y)
            if x + 1 < self.h:
                if its_one(x + 1, y):
                    self.check_point(x + 1, y)
            if y >= 1:
                if its_one(x, y - 1):
                    self.check_point(x, y - 1)
            if y + 1 < self.w:
                if its_one(x, y+1):
                    self.check_point(x, y + 1)

    def max_area_of_island(self, grid: List[List[int]]) -> int:

        self.h = len(grid)
        self.w = len(grid[0])
        self.grid = grid
        self.max_area = 0
        self.curr_area = 0

        for x in range(self.h):
            for y in range(self.w):
                if self.grid[x][y] == 1:
                    self.check_point(x, y)
                    self.max_area = max(self.max_area, self.curr_area)
                    self.curr_area = 0

        return self.max_area


def test():
    assert Solution().max_area_of_island([
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
    assert Solution().max_area_of_island([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
