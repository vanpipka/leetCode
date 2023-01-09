class Solution:
    def reverse_bits(self, n: int) -> int:

        a = "".join(reversed(str(bin(n)[2:])))
        a = (a + "00000000000000000000000000000000")[:32]

        return int(a, 2)


def test():
    pass