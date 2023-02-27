import string


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        _map = {str(i): i for i in range(10)}

        def get_int(_str):
            result = 0
            _pointer = 1
            while _pointer <= len(_str):
                d = _map[_str[-_pointer]]

                if _pointer == 1:
                    result += d
                else:
                    result += d * (10 ** (_pointer - 1))

                _pointer += 1

            return result

        return str(get_int(num1) * get_int(num2))


def test():
    assert Solution().multiply("35", "3") == 105
    assert Solution().multiply("5", "3") == 15

