class Solution:
    def is_power_of_two(self, n: int) -> bool:

        if 0 < n < 3:
            return True

        while 2 < n:
            if n % 2:
                return False
            n = n / 2

        return n == 2

def test():
    assert Solution().is_power_of_two(-64) is False
    assert Solution().is_power_of_two(1) is True
    assert Solution().is_power_of_two(16) is True
    assert Solution().is_power_of_two(3) is False
