from typing import List


class Solution:
    def unique_paths_with_obstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(len(obstacleGrid)):

            for x in range(len(obstacleGrid[i])):

                if i == 0 and x == 0:
                    obstacleGrid[i][x] = 1
                    continue
                if obstacleGrid[i][x] == 1:
                    obstacleGrid[i][x] = 0
                    continue
                if i == 0:
                    obstacleGrid[i][x] = obstacleGrid[i][x - 1]
                    continue
                if x == 0:
                    obstacleGrid[i][x] = obstacleGrid[i-1][x]
                    continue
                obstacleGrid[i][x] = obstacleGrid[i - 1][x] + obstacleGrid[i][x - 1]

        return obstacleGrid[-1][-1]


def test():
    assert Solution().unique_paths_with_obstacles([[0, 0], [1, 1], [0, 0]]) == 0
    assert Solution().unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
