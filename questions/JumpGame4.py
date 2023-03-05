from collections import defaultdict
from typing import List


class Solution:
    def min_jumps(self, arr: List[int]) -> int:

        n = len(arr)
        if n == 1:
            return 0

        _map = defaultdict(list)
        for i, num in enumerate(arr):
            _map[num].append(i)

        step = 0
        ways = {0}
        visited = set()

        while len(visited) <= len(arr):
            step += 1
            new_way = set()
            for i in ways:
                val = _map.get(arr[i], [])

                for x in val:
                    if x != i and x not in visited:
                        visited.add(x)
                        if x == len(arr)-1:
                            return step
                        new_way.add(x)

                _map[arr[i]] = []    # the most important thing!!!!

                if i-1 >= 0 and (i-1) not in visited:
                    visited.add(i-1)
                    new_way.add(i-1)
                if i+1 <= len(arr) and (i+1) not in visited:
                    visited.add(i+1)
                    if i+1 == len(arr)-1:
                        return step
                    new_way.add(i+1)

            ways = new_way

        return 0


def test():

    assert Solution().min_jumps([1, 2, 1, 6, 2, 1, 2, 7, 11, 6]) == 3
    assert Solution().min_jumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]) == 3
    assert Solution().min_jumps([7]) == 0
    assert Solution().min_jumps([7, 6, 9, 6, 9, 6, 9, 7]) == 1
