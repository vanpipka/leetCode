import collections
class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        rn = collections.Counter(ransomNote)
        mz = collections.Counter(magazine)

        for key, val in rn.items():
            if mz.get(key, 0) < val:
                return False

        return True



def test():
    assert Solution().can_construct("aa", "ab") is False
    assert Solution().can_construct("acb", "abac") is True