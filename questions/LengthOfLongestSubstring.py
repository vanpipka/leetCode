class Solution:
    def length_of_longest_substring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        stack = []
        res = 0
        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
                res = max(res, len(stack))
            else:
                stack = stack[stack.index(s[i]) + 1:] + [s[i]]
        return res


def test():
    assert Solution().length_of_longest_substring("abcabcbb") == 3
    assert Solution().length_of_longest_substring("bbbbb") == 1
    assert Solution().length_of_longest_substring("pwwkew") == 3
    assert Solution().length_of_longest_substring("aab") == 2
    assert Solution().length_of_longest_substring("dvdf") == 3
    assert Solution().length_of_longest_substring("au") == 2
