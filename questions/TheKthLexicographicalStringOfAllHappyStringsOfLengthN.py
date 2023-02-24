from typing import List


class Solution:
    def get_happy_string(self, n: int, k: int) -> str:

        symbols = ["a", "b", "c"]
        result = []

        def dfs(lst):

            if len(lst) == n:
                string = ("").join(lst)
                if string not in result:
                    result.append(string)
            if len(lst) > n:
                return

            for i in range(3):
                if lst and symbols[i] == lst[-1]:
                    continue
                lst.append(symbols[i])
                dfs(lst)
                lst.pop()

        dfs([])

        if k <= len(result):
            return sorted(result)[k-1]
        else:
            return ""


def test():
    assert Solution().get_happy_string(3, 9) == "cab"
