from typing import List


class Solution:
    def sort_sentence(self, s: str) -> str:
        add = s.split(" ")
        result = [None for _ in add]

        for i in add:
            result[int(i[-1])-1] = i[:-1]

        return (" ").join(result)
def test():
    assert Solution().sort_sentence("is2 sentence4 This1 a3") == "This is a sentence"

