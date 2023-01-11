import collections
class Solution:
    def can_construct(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        rn = collections.Counter(t)
        mz = collections.Counter(s)

        for key, val in rn.items():
            if mz.get(key, 0) < val:
                return False

        return True


def test():
    assert Solution().can_construct("anagram", "anagrma") is True
    assert Solution().can_construct("acb", "abac") is False
