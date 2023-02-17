from typing import List


class Solution:
    def cells_in_range(self, s: str) -> List[str]:
        result = []
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        start_c = int(s[1])
        start_r = alphabet.find(s[0])
        end_r = alphabet.find(s[3])

        while start_r <= end_r:
            while start_c <= int(s[4]):
                result.append(f"{alphabet[start_r]}{start_c}")
                start_c += 1
            start_c = int(s[1])
            start_r += 1

        print(result)

        return result
def test():
    assert Solution().cells_in_range("K1:L2") == ["K1", "K2", "L1", "L2"]

