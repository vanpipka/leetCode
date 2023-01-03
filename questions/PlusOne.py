from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:

        return [int(x) for x in str(int("".join([str(i) for i in digits]))+1)]
