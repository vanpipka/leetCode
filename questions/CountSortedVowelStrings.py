class Solution:
    def count_vowel_strings(self, n: int) -> int:

        dp = [[i for i in range(5, 0, -1)] for _ in range(n)]

        for i in range(1, len(dp)):
            for x in reversed(range(4)):
                dp[i][x] = dp[i-1][x] + dp[i][x+1]

        return dp[n - 1][0]


def test():
    assert Solution().count_vowel_strings(3) == 35
