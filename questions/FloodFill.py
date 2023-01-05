from typing import List


class Solution:

    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        h = len(image)
        w = len(image[0])

        old_color = image[sr][sc]

        if old_color == color:
            return image

        def change_color(x, y):

            if image[x][y] == old_color:
                image[x][y] = color
                if x >= 1:
                    change_color(x - 1, y)
                if x + 1 < h:
                    change_color(x + 1, y)
                if y >= 1:
                    change_color(x, y - 1)
                if y + 1 < w:
                    change_color(x, y + 1)

        change_color(sr, sc)

        return image


def test():
    assert Solution().flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2) \
           == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert Solution().flood_fill([[0, 0, 0], [0, 0, 0]], sr=1, sc=1, color=0) == [[0, 0, 0], [0, 0, 0]]
