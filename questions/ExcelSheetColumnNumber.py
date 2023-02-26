import string


class Solution:
    def title_no_number(self, columnTitle: str) -> int:
        _columnNumber = str(columnTitle)
        result = 0
        _map = {}
        alphabet = string.ascii_uppercase
        for i in range(1, len(alphabet)+1):
            _map[alphabet[i-1]] = i

        for i in range(len(_columnNumber)):
            result += (26 ** i) * _map[_columnNumber[-(i+1)]]

        return result


def test():
    assert Solution().title_no_number("FXSHRXW") == 2147483647
    assert Solution().title_no_number("AB") == 28
    assert Solution().title_no_number("B") == 2
    assert Solution().title_no_number("ZY") == 701

