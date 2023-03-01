from typing import List


class Solution:

    @staticmethod
    def merge_list(l1: List[int], l2: List[int]) -> List[int]:

        result = []
        x, y = 0, 0

        while x < len(l1) and y < len(l2):
            if l1[x]<l2[y]:
                result.append(l1[x])
                x += 1
            else:
                result.append(l2[y])
                y += 1

        return result + l1[x:] + l2[y:]

    def sort_array(self, nums: List[int]) -> List[int]:

        mid = len(nums) // 2
        l1, l2 = nums[:mid], nums[mid:]
        if len(l1) > 1:
            l1 = self.sort_array(nums[:mid])
        if len(l2) > 1:
            l2 = self.sort_array(nums[mid:])
        return Solution.merge_list(l1, l2)


def test():

    assert Solution().sort_array([5, 2, 3, 1]) == [1, 2, 3, 5]





