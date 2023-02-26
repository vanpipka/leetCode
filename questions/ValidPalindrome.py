import string


class Solution:
    def is_palindrome(self, s: str) -> bool:

        alphabet = {i for i in (string.ascii_lowercase + "0123456789")}
        s = s.lower()
        i, j = 0, len(s)-1

        while i<=j:
            if s[i] not in alphabet:
                i += 1
                continue
            if s[j] not in alphabet:
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


def test():
    assert Solution().is_palindrome("A man, a plan, a canal: Panama") is True
