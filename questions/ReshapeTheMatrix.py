from typing import List


class Solution:
    def matrix_reshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        if len(mat)*len(mat[0]) != r*c:
            return mat

        result = []
        i, j = 0, 0
        for x in range(r):
            row = []
            for y in range(c):

                if j == len(mat[0]):
                    i += 1
                    j = 0

                row.append(mat[i][j])
                j += 1

            result.append(row)

        return result


def test():
    assert Solution().matrix_reshape([[1, 2], [3, 4]], r=1, c=4) == [[1, 2, 3, 4]]
    assert Solution().matrix_reshape([[1, 2], [3, 4]], r=2, c=4) == [[1, 2], [3, 4]]

