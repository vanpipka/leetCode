import copy
from typing import List


class Solution:

    def __init__(self):

        self.h = 0
        self.w = 0

    def solve(self, board: List[List[str]]) -> None:

        self.h = len(board)
        self.w = len(board[0])

        def check_point(x, y):

            for coord in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if coord[0] < 0 or coord[1] < 0:
                    continue
                if coord[0] >= self.h or coord[1] >= self.w:
                    continue

                val = board[coord[0]][coord[1]]
                if val == "O":
                    board[coord[0]][coord[1]] = "#"
                    zero_lst.append((coord[0], coord[1]))
                    check_point(coord[0], coord[1])

        zero_lst = []

        for x in range(self.h):
            for y in range(self.w):
                if (x == 0 or x == self.h-1) and board[x][y] == "O":
                    zero_lst.append((x, y))
                    check_point(x, y)
                elif (y == 0 or y == self.w-1) and board[x][y] == "O":
                    zero_lst.append((x, y))
                    check_point(x, y)

        for x in range(self.h):
            for y in range(self.w):

                board[x][y] = "O" if (x, y) in zero_lst else "X"

        return board


def test():
    assert Solution().solve([["O", "O"], ["O", "O"]]) == [["O", "O"], ["O", "O"]]
    assert Solution().solve([
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]) == [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]

