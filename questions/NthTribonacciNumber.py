class Solution:
    def tribonacci(self, n: int) -> int:

        if n < 1:
            return n

        tr = [0, 1, 1]

        for i in range(2, n):
            tr.append(tr[-1]+tr[-2]+tr[-3])
        return tr[-1]


def test():
    assert Solution().tribonacci(4) == 4
    assert Solution().tribonacci(25) == 1389537
