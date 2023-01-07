from typing import List


class Solution:

    def __init__(self):
        self.result = []

    def perm(self, lst, n):
        if n < 2:
            self.result.append(lst.copy())
            return
        j = n-1
        while j >= 0:
            lst[j], lst[n-1] = lst[n-1], lst[j]
            self.perm(lst, n-1)
            lst[j], lst[n-1] = lst[n-1], lst[j]
            j -= 1

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.perm(nums, len(nums))

        print(self.result)
        return self.result


def test():
    assert Solution().permute([1, 2, 3]) == [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert Solution().permute([0, 1]) == [[0, 1], [1, 0]]
    assert Solution().permute([1]) == [[1]]
