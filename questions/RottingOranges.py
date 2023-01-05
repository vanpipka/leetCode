from typing import List


class Solution:
    def oranges_rotting(self, grid: List[List[int]]) -> int:

        def get_index(list, from_y):
            try:
                result_ = list.index(2, from_y)
            except:
                result_ = None

            return result_

        if grid == [[0]]:
            return 0

        h = len(grid)

        if h == 0:
            return 0

        w = len(grid[0])

        quique = []

        it_have_1 = False

        for x in range(h):

            if 1 in grid[x]:
                it_have_1 = True

            y = get_index(grid[x], 0)

            while y is not None:
                quique.append((x, y, 0))
                y = get_index(grid[x], y+1)

        if it_have_1 is not True:
            return 0

        if len(quique) == 0:
            return -1

        i = 0
        result = 0
        while i == 0:

            x, y, order = quique[i][0], quique[i][1], quique[i][2]
            result = max(result, order)
            quique.remove(quique[i])

            if x!=0:
                if grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    quique.append((x-1, y, order+1))
            if x+1<h:
                if grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    quique.append((x+1, y, order+1))
            if y!=0:
                if grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    quique.append((x, y-1, order+1))
            if y+1<w:
                if grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    quique.append((x, y+1, order+1))

            i = -1 if len(quique) == 0 else 0

        for x in grid:
            if 1 in x:
                return -1

        return result
