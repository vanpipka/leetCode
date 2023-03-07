from typing import Optional, List
from services.Structures import ListNode


class Solution:

    def minimum_time(self, time: List[int], totalTrips: int) -> int:

        start = 1
        end = min(time) * totalTrips

        while start < end:
            mid = (end + start) // 2
            if sum(mid // t for t in time) >= totalTrips:
                end = mid
            else:
                start = mid + 1

        return start

def test():
    assert Solution().minimum_time([1, 2, 3, 5, 7, 10], 5) == 3



