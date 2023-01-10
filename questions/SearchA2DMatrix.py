from typing import List


class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 0:
            return False

        if len(matrix) == 1:
            return target in matrix[0]

        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False

        for i in range(len(matrix)-1):
            if matrix[i][-1] < target < matrix[i+1][0]:
                return False
            if matrix[i][0] <= target <= matrix[i][-1]:
                return target in matrix[i]

        return target in matrix[i+1]


def test():
    assert Solution().search_matrix([[1], [3]], 1) is True
    assert Solution().search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 30) is True
