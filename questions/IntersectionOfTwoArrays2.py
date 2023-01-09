from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        map1, map2 = {}, {}
        result = []

        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                map1[nums1[i]] = map1.get(nums1[i], 0) + 1
            if i < len(nums2):
                map2[nums2[i]] = map2.get(nums2[i], 0) + 1

        for x, y in map1.items():

            for i in range(y):
                if not map2.get(x) is None and map2[x] > 0:
                    result.append(x)
                    map2[x] = map2[x] - 1

        return result


def test():

    assert Solution().intersect([4, 9, 5, 4], [9, 4, 9, 8, 4]) == [4, 4, 9]
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
