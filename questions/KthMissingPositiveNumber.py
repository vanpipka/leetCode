from typing import List


class Solution:
    def find_kth_positive(self, arr: List[int], k: int) -> int:
        i = 1
        pos = 0
        while True:
            if k == 0:
                return i - 1
            if pos < len(arr) and i == arr[pos]:
                pos += 1
            else:
                k -= 1
            i += 1


def test():
    assert Solution().find_kth_positive([2,3,4,7,11], k = 5) == 9



