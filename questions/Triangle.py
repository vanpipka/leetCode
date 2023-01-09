from typing import List


class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:

        for i in reversed(range(len(triangle)-1)):
            for x in range(len(triangle[i])):
                triangle[i][x] = triangle[i][x] + min(triangle[i+1][x], triangle[i+1][x+1])

        return triangle[0][0]


def test():
    assert Solution().minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert Solution().minimum_total([[-10]]) == -10
    assert Solution().minimum_total(
    [[-7],
     [-2, 1],
     [-5, -5, 9],
     [-4, -5, 4, 4],
     [-6, -6, 2, -1, -5],
     [3, 7, 8, -3, 7, -9],
     [-9, -1, -9, 6, 9, 0, 7],
     [-7, 0, -6, -8, 7, 1, -4, 9],
     [-3, 2, -6, -9, -7, -6, -9, 4, 0],
     [-8, -6, -3, -9, -2, -6, 7, -5, 0, 7],
     [-9, -1, -2, 4, -2, 4, 4, -1, 2, -5, 5],
     [1, 1, -6, 1, -2, -4, 4, -2, 6, -6, 0, 6],
     [-3, -3, -6, -2, -6, -2, 7, -9, -5, -7, -5, 5, 1]]) == -63
