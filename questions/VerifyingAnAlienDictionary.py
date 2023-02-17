from typing import List


class Solution:
    def is_alien_sorted(self, words: List[str], order: str) -> bool:

        hash = {order[i]: i for i in range(len(order))}
        position = 0

        for i in range(len(words)-1):
            for j in range(len(words[i])):

                if j >= len(words[i+1]):
                    return False

                if words[i][j] != words[i+1][j]:
                    if hash[words[i][j]] > hash[words[i+1][j]]:
                        return False
                    break

        return True


def test():
    assert Solution().is_alien_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") is False
    assert Solution().is_alien_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") is True
    assert Solution().is_alien_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") is False
