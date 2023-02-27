import string


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        _map = {str(i): i for i in range(10)}

        if len(num1) < len(num2):
            num1 = "0"*(len(num2) - len(num1)) + num1
        if len(num2) < len(num1):
            num2 = "0"*(len(num1) - len(num2)) + num2

        result = 0
        _pointer = 1
        while _pointer <= len(num1):
            d = _map[num1[-_pointer]]
            d1 = _map[num2[-_pointer]]

            if _pointer == 1:
                result += (d + d1)
            else:
                result += (d + d1) * (10**(_pointer-1))

            _pointer += 1

        return result


def test():
    assert Solution().multiply("11", "123") == 134
    assert Solution().multiply("35", "3") == 38
    assert Solution().multiply("5", "3") == 8
    assert Solution().multiply("123", "456") == 579
