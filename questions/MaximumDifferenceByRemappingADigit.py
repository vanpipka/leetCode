class Solution:
    def min_max_difference(self, num: int) -> int:
        _num = str(num)
        _min, _max = [], []
        x, y = "", ""
        for i in range(len(_num)):
            if not x:
                if _num[i] != "9":
                    x = _num[i]
                _max.append("9")
            elif _num[i] == x:
                _max.append("9")
            else:
                _max.append(_num[i])

            if not y:
                y = _num[i]
            elif _num[i] == y:
                if _min:
                    _min.append("0")
            else:
                _min.append(_num[i])

        if not _min:
            _min.append("0")
        if not _max:
            _max.append("0")

        return int(("").join(_max)) - int(("").join(_min))


def test():
    assert Solution().min_max_difference("90") == 99
    assert Solution().min_max_difference("11891") == 99009
