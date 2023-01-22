from typing import List


class Solution:
    def set_zeroes(self, matrix: List[List[int]]) -> None:

        rows, cols = [], []

        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                if matrix[i][x] == 0:
                    if i not in rows:
                        rows.append(i)
                    if x not in cols:
                        cols.append(x)

        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                if i in rows:
                    matrix[i][x] = 0
                if x in cols:
                    matrix[i][x] = 0

        return matrix


def test():
    assert Solution().set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert Solution().set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
