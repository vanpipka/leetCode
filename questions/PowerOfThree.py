class Solution:
    def is_power_of_three(self, n: int) -> bool:

        if n == 1:
            return True

        if n < 3:
            return False

        while 3 < n:
            if n % 3:
                return False
            n = n / 3

        return n == 3

def test():
    assert Solution().is_power_of_three(-64) is False
    assert Solution().is_power_of_three(27) is True
    assert Solution().is_power_of_three(3) is True
    assert Solution().is_power_of_three(7) is False
