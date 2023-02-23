from collections import Counter
from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:

        #
        # ans = []
        #
        # for i in range(n + 1):
        #     ans.append(Counter(bin(i)).get("1", 0))
        # return ans

        # right:

        dp = [0]
        for i in range(1, n + 1):
            dp.append(dp[i >> 1] + i % 2)
        return dp


def test():
    assert Solution().count_bits(2) == [0, 1, 1]
    assert Solution().count_bits(5) == [0, 1, 1, 2, 1, 2]
