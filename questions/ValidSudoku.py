import collections
from typing import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:

        horizontal = []
        vertical = []
        cube = []

        for x in range(9):
            y_pos = 0
            for y in range(9):

                if board[x][y] in horizontal or board[y][x] in vertical:
                    return False

                if y % 3 == 0:
                    cube.clear()

                if board[x][y] != ".":
                    horizontal.append(board[x][y])
                if board[y][x] != ".":
                    vertical.append(board[y][x])

                if x % 3 == 0:
                    for z in range(3):
                        if board[x+z][y] != ".":
                            if board[x+z][y] in cube:
                                return False
                            cube.append(board[x+z][y])

            horizontal.clear()
            vertical.clear()

        return True

def test():
    assert Solution().is_valid_sudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", "3", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is False
