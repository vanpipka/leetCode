from typing import List


class Solution:
    def sort_people(self, names: List[str], heights: List[int]) -> List[str]:

        _map = list(zip(names, heights))

        return [i[0] for i in sorted(_map, key=lambda x: x[1], reverse=True)]


def test():
    assert Solution().sort_people(["Mary", "John", "Emma"], [180, 165, 170]) == ["Mary", "Emma", "John"]



