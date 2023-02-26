import string


class Solution:
    def is_palindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                string1 = s[:i] + s[i + 1:]
                string2 = s[:j] + s[j + 1:]
                return string1 == string1[::-1] or string2 == string2[::-1]

            i += 1
            j -= 1

        return True


def test():
    assert Solution().is_palindrome("amanaplanacanalptanama") is True
