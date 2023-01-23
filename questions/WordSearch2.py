from __future__ import annotations
from typing import List
import copy


class TrieNode:

    def __init__(self):
        self._children = {}
        self._end = False

    def add_child(self, child: str) -> TrieNode:
        new_child = TrieNode()
        self._children[child] = new_child
        return new_child

    def get_child(self, child: str) -> TrieNode:
        return self._children.get(child, None)

    def remove_child(self, child: str) -> None:
        return self._children.pop(child)

    def get_children(self) -> dict[TrieNode]:
        return self._children

    def set_end(self) -> None:
        self._end = True

    def get_end(self) -> bool:
        return self._end

class Solution:

    def __init__(self):

        self.h = 0
        self.w = 0
        self.trie_root = TrieNode()

    def build_a_tree(self, words):

        for word in words:
            cur = self.trie_root
            for char in word:
                child = cur.get_child(char)
                if not child:
                    child = cur.add_child(char)
                cur = child
            cur.set_end()

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.build_a_tree(words)
        self.h = len(board)
        self.w = len(board[0])

        def check_point(x, y, node, search_word):

            if node.get_end():
                result.add(search_word)
                if len(node.get_children()) == 0:
                    return True

            lt = matrix[x][y]
            matrix[x][y] = ''

            if x >= 1:

                val = matrix[x-1][y]
                child = node.get_child(matrix[x-1][y])
                if child:
                    done = check_point(x-1, y, child, search_word+val)
                    if done:
                        node.remove_child(val)
                        matrix[x][y] = lt

            if x + 1 < self.h:

                val = matrix[x + 1][y]
                child = node.get_child(matrix[x + 1][y])
                if child:
                    done = check_point(x + 1, y, child, search_word+val)
                    if done:
                        node.remove_child(val)
                        matrix[x][y] = lt

            if y >= 1:

                val = matrix[x][y - 1]
                child = node.get_child(matrix[x][y - 1])
                if child:
                    done = check_point(x, y - 1, child, search_word+val)
                    if done:
                        node.remove_child(val)
                        matrix[x][y] = lt

            if y + 1 < self.w:

                val = matrix[x][y + 1]
                child = node.get_child(matrix[x][y + 1])

                if child:
                    done = check_point(x, y + 1, child, search_word+val)
                    if done:
                        node.remove_child(val)
                        matrix[x][y] = lt

            matrix[x][y] = lt

        result = set()
        matrix = copy.deepcopy(board)

        for x in range(self.h):
            for y in range(self.w):
                val = matrix[x][y]
                child = self.trie_root.get_child(matrix[x][y])
                if child:
                    check_point(x, y, child, val)

        print(list(result))

        return sorted(list(result))


def test():

    assert Solution().find_words([
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]) == sorted(["eat", "oath"])

    assert Solution().find_words([
        ["a"],
        ["c"]], ["aab", "ac", "aac"]) == sorted(["ac"])

    assert Solution().find_words([
        ["a", "b"],
        ["a", "a"]], ["baa","bab","aaab","aaa","aaaa","aaba"]) == sorted(['aaba', 'aaab', 'aaa', 'baa'])

    assert Solution().find_words([
        ["b"],
        ["a"],
        ["b"],
        ["b"],
        ["a"]], ["abba"]) == ["abba"]
    assert Solution().find_words([
        ["a", "a"],
        ["a", "a"]], ["aaaaa"]) == []
    assert Solution().find_words([
        ["a", "b"],
        ["c", "d"]], ["abcb"]) == []
