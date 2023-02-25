class Solution:

    def longest_palindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        result = s[0]

        for i in range(len(s)):

            x, y = i-1, i+1
            curr_str = [s[i]]
            maximum = 1

            end = min(len(s), i * 2 + 1)

            while y < end:
                if s[x] == s[y]:
                    curr_str.insert(0, s[x])
                    curr_str.append(s[y])
                    if len(curr_str) > len(result):
                        result = ("").join(curr_str)
                else:
                    break
                x -= 1
                y += 1

            x, y = i, i + 1

            curr_str = []
            maximum = 0

            end = min(len(s), i * 2 + 2)

            while y < end:
                if s[x] == s[y]:
                    curr_str.insert(0, s[x])
                    curr_str.append(s[y])
                    maximum = maximum+2
                    if len(curr_str) > len(result):
                        result = ("").join(curr_str)
                else:
                    break
                x -= 1
                y += 1

        return result


def test():
    assert Solution().longest_palindrome("ccc") == "ccc"
    assert Solution().longest_palindrome("bb") == "bb"
    assert Solution().longest_palindrome("cbbd") == "bb"
    assert Solution().longest_palindrome("abbad") == "abba"
    assert Solution().longest_palindrome("babad") == "bab"


