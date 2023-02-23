class Solution:
    def divisor_game(self, n: int) -> bool:
        return n%2 == 0


def test():
    assert Solution().divisor_game(3) is False
