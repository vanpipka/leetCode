from typing import List


class Solution:
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        hash = {i: True for i in jewels}
        result = 0
        for i in stones:
            if hash.get(i):
                result += 1

        return result


def test():
    assert Solution().num_jewels_in_stones("aA", "aAAbbbb") == 3
