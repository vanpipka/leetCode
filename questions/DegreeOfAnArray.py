from typing import List


class Solution:
    def find_shortest_sub_array(self, nums: List[int]) -> int:
        map: dict = {}
        max_degree = 1
        result = len(nums)

        for i in range(len(nums)):
            elem = nums[i]
            a = map.get(elem)
            if a:
                a[1] = i
                a[2] += 1
                max_degree = max(a[2], max_degree)
            else:
                map[elem] = [i, i, 1]

        for _, i in map.items():
            if i[2] == max_degree:
                result = min(result, i[1]-i[0]+1)

        return result


def test():
    assert Solution().find_shortest_sub_array([1, 2, 2, 3, 1]) == 2
    assert Solution().find_shortest_sub_array([1, 2, 2, 3, 1, 4, 2]) == 6

