class Solution:
    def unique_paths(self, m: int, n: int) -> int:

        if m == 1 or n == 1:
            return 1

        lst = []
        for x in range(m):
            for y in range(n):
                if x == 0 and y == 0:
                    lst.append([0])
                elif x == 0:
                    lst[0].append(1)
                elif y == 0:
                    lst.append([1])
                else:
                    lst[x].append(lst[x-1][y]+lst[x][y-1])

        return lst[m-1][n-1]


def test():
    assert Solution().unique_paths(3, 7) == 28
