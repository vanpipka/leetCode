class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        is_positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not is_positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


def test():
    assert Solution().divide(-2147483648, 2) == 2147483647
    assert Solution().divide(10, 3) == 3
    assert Solution().divide(-1, 1) == -1
