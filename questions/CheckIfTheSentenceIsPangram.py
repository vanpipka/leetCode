from typing import List


class Solution:
    def check_if_pangram(self, sentence: str) -> bool:

        return len(set(sentence)) == 26


def test():
    assert Solution().check_if_pangram("thequickbrownfoxjumpsoverthelazydog") == True

