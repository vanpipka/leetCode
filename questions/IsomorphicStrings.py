from typing import List


class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dct_s, dct_t = {}, {}

        for i in range(len(s)):
            if t[i] not in dct_t and s[i] not in dct_s:
                dct_s[s[i]] = t[i]
                dct_t[t[i]] = s[i]

            if t[i] != dct_s.get(s[i]) or s[i] != dct_t.get(t[i]):
                return False

        return True


def test():
    assert Solution().is_isomorphic(s="title", t="paper") is True
    assert Solution().is_isomorphic(s="badc", t="baba") is False
    assert Solution().is_isomorphic(s="egg", t="add") is True
    assert Solution().is_isomorphic(s="foo", t="bar") is False
