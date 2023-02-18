class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        lst = []
        st = ""
        fr = 0
        to = numRows + (numRows - 2)
        step = to
        result = ""

        while fr < len(s):
            lst.append(s[fr:to])
            fr += step
            to += step

        if s[fr:]:
            lst.append(s[fr:to])

        x = 0
        y = step

        for i in (range(numRows)):

            for j in range(len(lst)):

                if i == 0:
                    result += lst[j][i]
                else:
                    if x >= len(lst[j]):
                        continue
                    result += lst[j][x]
                    if x == y:
                        continue
                    if y < len(lst[j]):
                        result += lst[j][y]

            x += 1
            y -= 1

        print(result)
        return result


def test():

    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

