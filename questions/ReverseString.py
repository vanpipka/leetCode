from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:

        pos = len(s)-1

        while pos > 0:
            pos -= 1
            s.append(s.pop(pos))

        return s


def test():
    assert Solution().reverse_string(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    assert Solution().reverse_string(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]