import string
from typing import List


class Solution:
    def construct_rectangle(self, area: int) -> List[int]:

        half = int(area**0.5)

        while half > 0:
            if not area % half:
                return [area//half, half]
            half -= 1
        return [area, 1]

        string.ascii_lowercase

def test():
    assert Solution().construct_rectangle(4) == [2, 2]
    assert Solution().construct_rectangle(37) == [37, 1]
    assert Solution().construct_rectangle(122122) == [427, 286]
    assert Solution().construct_rectangle(45) == [9, 5]

