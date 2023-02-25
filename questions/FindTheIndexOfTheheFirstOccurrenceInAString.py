class Solution:
    def str_str(self, haystack: str, needle: str) -> int:

        len_h = len(haystack)
        len_n = len(needle)
        if len_h < len_n:
            return -1

        for i in range(len_h - len_n + 1):
            if needle == haystack[i:i+len_n]:
                return i

        return -1


def test():
    assert Solution().str_str("hell", "ll") == 2



