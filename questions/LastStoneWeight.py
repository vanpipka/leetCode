from typing import List


class Solution:
    def last_stone_weight(self, stones: List[int]) -> int:

        while True:
            if len(stones) == 1:
                return stones[0]
            if len(stones) == 0:
                return 0

            stones.sort()
            s_1 = stones.pop()
            s_2 = stones.pop()

            if s_1 != s_2:
                stones.append(s_1-s_2)

def test():

    assert Solution().last_stone_weight([2, 7, 4, 1, 8, 1]) == 1

