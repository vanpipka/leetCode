class Solution:
    def first_uniq_char(self, s: str) -> int:

        uniq = (i for i in s if s.count(i) == 1)

        try:
            d = next(uniq)
            return s.index(d)
        except StopIteration:
            return -1


def test():
    assert Solution().first_uniq_char("leetcode") == 0
    assert Solution().first_uniq_char("loveleetcode") == 2
    assert Solution().first_uniq_char("aabb") == -1
