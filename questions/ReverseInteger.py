class Solution:
    def reverse(self, x: int) -> int:

        if x < -2**31:
            return 0
        if x > 2**31 - 1:
            return 0

        data = str(x)

        if data[0] == '-':
            data = '-' + ''.join(reversed(data[1:]))
        else:
            data = ''.join(reversed(data))

        result = int(data)

        if result < -2 ** 31:
            return 0
        if result > 2 ** 31 - 1:
            return 0

        return result


def test():
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(900000) == 9
