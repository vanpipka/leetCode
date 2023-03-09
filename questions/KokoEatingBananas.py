from typing import List


class Solution:
    def min_eating_speed(self, piles: List[int], h: int) -> int:

        start = 1
        end = max(piles)
        result = end

        def get_hours(count):
            hours = 0

            for i in piles:
                if i <= count:
                    hours += 1
                else:
                    hours += i // count + (1 if i % count else 0)
            return hours

        while start < end:
            mid = (start + end) // 2
            hours = get_hours(mid)

            if hours > h:
                start = mid+1
            else:
                result = min(result, mid)
                end = mid

        return result


def test():
    assert Solution().min_eating_speed([1000000000], 2) == 500000000
    assert Solution().min_eating_speed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316,
     877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818) == 14
    assert Solution().min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert Solution().min_eating_speed([3, 6, 7, 11], 8) == 4




