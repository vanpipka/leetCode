import collections


class Solution:
    def longest_palindrome(self, s: str) -> int:

        data = collections.Counter(s)
        result = 0
        add = 0
        for key, val in data.items():

            if val == 1:
                add = 1
            elif val % 2 == 0:
                result += val
            else:
                result += (val - 1)
                add = 1

        return result+add


def test():
    assert Solution().longest_palindrome("ccc") == 3
    assert Solution().longest_palindrome("Aabccccdd") == 7
    assert Solution().longest_palindrome("Aa") == 1