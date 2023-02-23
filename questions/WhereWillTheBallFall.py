from typing import List


class Solution:
    def find_ball(self, grid: List[List[int]]) -> List[int]:

        width = len(grid[0])

        balls = [(0, i) for i in range(width)]

        for i in range(len(grid)):
            for x in range(width):
                for y in range(width):
                    ball = balls[y]
                    if ball[0] == i and ball[1] == x:
                        if grid[i][x] == 1:
                            if x+1 == width or grid[i][x+1] == -1:
                                continue
                        if grid[i][x] == -1:
                            if x-1 < 0 or grid[i][x-1] == 1:
                                continue
                        balls[y] = (i+1, x + grid[i][x])

        return [i[1] if i[0] == len(grid) else -1 for i in balls]


def test():
    assert Solution().find_ball([[1, 1, 1, 1, 1, 1],
                                 [-1, -1, -1, -1, -1, -1],
                                 [1, 1, 1, 1, 1, 1],
                                 [-1, -1, -1, -1, -1, -1]]) == [0, 1, 2, 3, 4, -1]
    assert Solution().find_ball([[1,1,1,-1,-1],
                                  [1,1,1,-1,-1],
                                  [-1,-1,-1,1,1],
                                  [1,1,1,1,-1],
                                  [-1,-1,-1,-1,-1]]) == [1,-1,-1,-1,-1]
