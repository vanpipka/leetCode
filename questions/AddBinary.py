class Solution:

    def add_binary(self, a: str, b: str) -> str:

        lengths_div = len(a) - len(b)
        result = ""
        add = "0"

        if lengths_div < 0:
            a = "0" * (-(len(a) - len(b))) + a
        else:
            b = "0" * (len(a) - len(b)) + b

        for i in reversed(range(len(a))):

            if b[i] == a[i] == "0":
                result = add + result
                add = "0"
            elif b[i] == a[i] == "1":
                result = add + result
                add = "1"
            else:
                result = ("0" if add == "1" else "1") + result

        if add == "1":
            result = "1"+result

        return result


def test():
    assert Solution().add_binary("11", "1") == "100"
    assert Solution().add_binary("10", "10011") == "10101"
    assert Solution().add_binary("1010", "1011") == "10101"



