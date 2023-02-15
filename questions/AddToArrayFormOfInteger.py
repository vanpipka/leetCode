from typing import List


class Solution:

    def add_to_array_form(self, num: List[int], k: int) -> List[int]:

        return [int(i) for i in str(k+int(("").join([str(i) for i in num])))]


def test():
    assert Solution().add_to_array_form([1, 2, 0, 0], 34) == [1, 2, 3, 4]




