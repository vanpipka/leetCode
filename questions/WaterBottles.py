class Solution:
    def num_water_bottles(self, numBottles: int, numExchange: int) -> int:

        result = numBottles
        x = numBottles

        change = 0

        while x >= numExchange:

            empty = x+change
            x = empty//numExchange
            result += x

            x += empty - x*numExchange

        return result


def test():
    assert Solution().num_water_bottles(9, 3) == 13
    assert Solution().num_water_bottles(15, 4) == 19