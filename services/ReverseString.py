from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:

        pos = len(s)-1

        while pos > 0:
            pos -= 1
            s.append(s.pop(pos))

        return s

