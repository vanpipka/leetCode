from typing import List


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False

        pos_t = 0
        res = ""

        for i in s:

            while pos_t < len(t):
                pos_t += 1
                if t[pos_t-1] == i:
                    res += i
                    break

            if res == s:
                return True

        return res == s


def test():
    assert Solution().is_subsequence(s="abc", t="ahbgdc") is True
    assert Solution().is_subsequence(s="axc", t="ahbgdc") is False
