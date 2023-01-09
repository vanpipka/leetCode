class Solution:
    def hamming_weight(self, n: int) -> int:

        return str(bin(n)).count("1")


def test():
    assert Solution().hamming_weight("00000000000000000000000000001011") == 3