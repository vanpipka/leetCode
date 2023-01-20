from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[int]:

        nums = sorted(nums)

        if nums[0] > 0 or nums[-1] < 0:
            return []

        if len(nums) >= 3 and len([i for i in nums if i != 0]) == 0:
            return [[0, 0, 0]]

        result = []

        for i in range(len(nums)-2):
            x = len(nums)-1
            y = i+1
            while abs(nums[i]+nums[y]) > nums[-1]:
                if y == x:
                    break
                y += 1

            for y in range(y, len(nums)-1):

                if y == x:
                    break

                tmp = nums[i] + nums[y]

                if tmp > 0:
                    break

                while tmp + nums[x] >= 0:
                    if tmp + nums[x] == 0:
                        lst = sorted([nums[i], nums[y], nums[x]])
                        if lst not in result:
                            result.append(lst)
                    x -= 1
                    if y == x:
                        break
        print(result)
        return result


def test():

    assert Solution().three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) ==\
           [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
    assert Solution().three_sum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    assert Solution().three_sum([3, -2, 1, 0]) == []
    assert Solution().three_sum([-1, 0, 1, 2, -1, -5, 11]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().three_sum([4, 4, -1, 4, -1]) == []
    assert Solution().three_sum([1, 1, 1]) == []


