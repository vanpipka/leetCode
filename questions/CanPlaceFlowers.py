from typing import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:

        len_flowerbed = len(flowerbed)

        if len_flowerbed == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            if flowerbed[0] == 1 and n == 0:
                return True
            return False

        for i in range(len_flowerbed):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len_flowerbed - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            if n <= 0:
                return True

        return False


def test():
    assert Solution().can_place_flowers([1, 0, 0, 0, 1], 1) is True
    assert Solution().can_place_flowers([1, 0, 0, 0, 1], 2) is False
