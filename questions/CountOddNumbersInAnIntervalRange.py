class Solution:

    def count_odds(self, low: int, high: int) -> int:

        result = 0
        count = high-low+1
        if low % 2 == 0:
            result = count//2
        else:
            result = (count+1)//2

        print(result)

        return result


def test():

    assert Solution().count_odds(3, 7) == 3
    assert Solution().count_odds(1, 2) == 1
    assert Solution().count_odds(8, 10) == 1
    assert Solution().count_odds(4, 8) == 2

