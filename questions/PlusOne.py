from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:

        return [int(x) for x in str(int("".join([str(i) for i in digits]))+1)]


def test():
    assert Solution().plus_one([1, 2, 3]) == [1, 2, 4]
    assert Solution().plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution().plus_one([9]) == [1, 0]
