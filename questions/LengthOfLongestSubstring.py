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

