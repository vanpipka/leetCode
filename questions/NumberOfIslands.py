from typing import List


class Solution:

    def __init__(self):
        self.h = 0
        self.w = 0
        self.grid = []
        self.pointer = 0

    def check_point(self, x, y):

        def its_one(x_, y_):
            return self.grid[x_][y_] == 1

        if self.grid[x][y] == 1:
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

    def num_islands(self, grid: List[List[int]]) -> int:

        self.h = len(grid)
        self.w = len(grid[0])
        self.grid = grid
        pointer = 0

        for x in range(self.h):
            for y in range(self.w):
                if self.grid[x][y] == 1:
                    self.check_point(x, y)
                    pointer += 1

        return pointer


def test():

    assert Solution().num_islands([
              [1, 1, 1, 1, 0],
              [1, 1, 0, 1, 0],
              [1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0]]) == 1

    assert Solution().num_islands([
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
    assert Solution().num_islands([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
