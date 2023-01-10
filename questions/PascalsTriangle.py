from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pointer = 1
        result = []

        for i in range(numRows):
            row = [1]
            for x in range(1, pointer):
                if x == pointer-1:
                    row.append(1)
                else:
                    row.append(result[i-1][x-1]+result[i-1][x])
            pointer += 1
            result.append(row)

        return result

def test():
    assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
