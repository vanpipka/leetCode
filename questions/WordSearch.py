from typing import List
import copy


class Solution:

    def __init__(self):
        self.word = ""
        self.curr_word = ""
        self.board = []
        self.h = 0
        self.w = 0

    def check_point(self, x, y, position):

        if self.curr_word == self.word:
            return

        if position >= len(self.word):
            return

        self.curr_word = self.curr_word[:position]

        def its_one(x_, y_):

            if position >= len(self.word):
                return

            return self.board[x_][y_] == self.word[position]

        if self.board[x][y] == self.word[position]:

            self.curr_word += self.word[position]
            position += 1

            curr = self.board[x][y]
            self.board[x][y] = None

            if x >= 1:
                if its_one(x - 1, y):
                    a1 = self.check_point(x - 1, y, position)
            if x + 1 < self.h:
                if its_one(x + 1, y):
                    a2 = self.check_point(x + 1, y, position)
            if y >= 1:
                if its_one(x, y - 1):
                    b1 = self.check_point(x, y - 1, position)
            if y + 1 < self.w:
                if its_one(x, y+1):
                    b2 = self.check_point(x, y + 1, position)

            self.board[x][y] = curr

    def exist(self, board: List[List[str]], word: str) -> bool:

        self.curr_word = ""
        self.word = word
        self.board = copy.deepcopy(board)
        self.h = len(board)
        self.w = len(board[0])

        first_symbol = word[0]
        all_characters = ""
        for x in self.board:
            all_characters += "".join(x)

        for i in set(word):
            if all_characters.find(i) == -1:
                return False

        for x in range(len(self.board)):
            if first_symbol not in self.board[x]:
                continue

            for y in range(len(self.board[x])):

                if self.board  != board:
                    self.board = copy.deepcopy(board)
                self.curr_word = ""

                if self.board[x][y] == first_symbol:
                    self.check_point(x, y, 0)

                    if self.curr_word == word:
                        break

            if self.curr_word == word:
                break

        return self.curr_word == word
