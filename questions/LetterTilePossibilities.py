from typing import List


class Solution:
    def num_tile_possibilities(self, tiles: str) -> int:

        result = set()

        def dfs(lst, _tiles):

            if lst:
                result.add(("").join(lst))

            for i in range(len(_tiles)):
                lst.append(_tiles[i])
                dfs(lst, _tiles[:i]+_tiles[i+1:])
                lst.pop()

        dfs([], tiles)

        return len(result)


def test():
    assert Solution().num_tile_possibilities("AAB") == 8
