class Solution:
    def hamming_weight(self, n: int) -> int:

        return str(bin(n)).count("1")


def test():
    pass