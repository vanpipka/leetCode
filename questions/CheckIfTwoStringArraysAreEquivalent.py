from typing import List


class Solution:
    def array_strings_are_equal(self, word1: List[str], word2: List[str]) -> bool:

        return ("").join(word1) == ("").join(word2)

def test():
    assert Solution().array_strings_are_equal(["ab", "c"], ["a", "bc"]) is True

