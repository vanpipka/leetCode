from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:

        lowest_price = float('inf')
        max_profit = 0

        for price in prices:
            lowest_price = min(price, lowest_price)
            max_profit = max(max_profit, (price - lowest_price))

        return max_profit


def test():
    assert Solution().max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().max_profit([2, 1, 2, 1, 0, 1, 2]) == 2
    assert Solution().max_profit([7, 6, 4, 3, 1]) == 0

