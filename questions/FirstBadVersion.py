# The isBadVersion API is already defined for you.



class Solution:

    @staticmethod
    def is_bad_version(version: int) -> bool:
        return True

    def first_bad_version(self, n: int) -> int:

        result = 0
        low = 0
        high = n

        while low <= high:
            mid = (low+high) // 2
            if self.is_bad_version(mid):
                result = mid
                high = mid-1
            else:
                low = mid+1

        return 0
        # return result  # -use it for leetcode
