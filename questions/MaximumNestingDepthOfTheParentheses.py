from typing import List


class Solution:
    def max_depth(self, s: str) -> int:
        maximum = 0
        counter = 0

        for i in s:
            if i == "(":
                counter += 1
                maximum = max(maximum, counter)
            elif i == ")":
                counter -=1

        return maximum


def test():
    assert Solution().max_depth("(1)+((2))+(((3)))") == 3

