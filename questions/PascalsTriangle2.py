from typing import List


class Solution:
    def get_row(self, rowIndex: int) -> List[int]:

        rows = [[1], [1, 1]]
        if rowIndex < 2:
            return rows[rowIndex]

        for i in range(2, rowIndex+1):
            row = [1 for _ in range(i+1)]
            for x in range(1, i):
                row[x] = rows[i-1][x-1] + rows[i-1][x]

            rows.append(row)
        return rows[-1]


def test():
    assert Solution().get_row(3) == [1, 3, 3, 1]