from typing import List


class Solution:
    def read_binary_watch(self, turnedOn: int) -> List[str]:

        res = []
        led = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]

        def dfs(h, m, idx, n):
            nonlocal res
            if h > 11 or m > 59:
                return
            if n == 0:
                res.append("{:d}:{:02d}".format(h, m))
                return
            for i in range(idx, len(led)):  # <- right here, we can just iterate through the options we have
                if i <= 3:
                    dfs(h + led[i], m, i + 1, n - 1)
                elif i < len(led):
                    dfs(h, m + led[i], i + 1, n - 1)

        dfs(0, 0, 0, turnedOn)
        return res


def test():
    assert Solution().read_binary_watch(1) == ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    # assert Solution().read_binary_watch(2) == ["0:01", "0:02", "0:04", "0:08",
    # "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]