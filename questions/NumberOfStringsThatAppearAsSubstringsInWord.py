from typing import List


class Solution:
    def num_of_strings(self, patterns: List[str], word: str) -> int:
        result = 0
        for i in patterns:
            if i in word:
                result += 1
        return result


def test():
    assert Solution().num_of_strings(["a", "abc", "bc", "d"], "abc") == 3
