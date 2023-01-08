from typing import List
import math


class Solution:

    def __init__(self):

        self.result = []
        self.s = 0
    def perm(self, lst, n):
        if n < 2:
            if lst not in self.result and sum(lst) >= self.s:
                self.result.append(lst.copy())
            return
        j = n - 1
        while j >= 0:
            lst[j], lst[n - 1] = lst[n - 1], lst[j]
            self.perm(lst, n - 1)
            lst[j], lst[n - 1] = lst[n - 1], lst[j]
            j -= 1

    def climb_stairs(self, s: str) -> List[str]:

        if s<=3:
            return s

        result = 1

        curr_lst = [1 for i in range(s)]

        while True:
            if curr_lst[-2:] == [1, 1]:
                curr_lst = [2]+curr_lst[:-2]
                result += math.factorial(len(curr_lst))/(math.factorial(curr_lst.count(1))*math.factorial(curr_lst.count(2)))
            else:
                break

        return int(result)


def test():
    #assert Solution().climb_stairs(2) == 2
    #assert Solution().climb_stairs(3) == 3
    #assert Solution().climb_stairs(4) == 5
    #assert Solution().climb_stairs(5) == 8
    assert Solution().climb_stairs(6) == 13