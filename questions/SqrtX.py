class Solution:
    def my_sqrt(self, x: int) -> int:

        left, right, root = 0, x, -1
        while left <= right:
            mid = (right + left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                root = mid
                left = mid + 1
            else:
                right = mid - 1
        return root


def test():

    assert Solution().my_sqrt(8) == 2
