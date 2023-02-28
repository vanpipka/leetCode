from typing import List


class Solution:

    def __init__(self):
        self.weights = []

    def days_per_capacity(self, capacity: int) -> bool:

        _weights = self.weights.copy()

        days = 0
        _capacity = capacity
        i = 0
        while i < len(_weights):

            if _weights[i] > capacity:
                return 0

            _capacity -= _weights[i]
            if _capacity < 0:
                _capacity = capacity
                days += 1
                continue
            _weights[i] = 0
            if i == len(_weights) - 1:
                days += 1
            i += 1

        return days if sum(_weights) == 0 else 0

    def ship_within_days(self, weights: List[int], days: int) -> int:

        self.weights = weights

        _min = max(self.weights)
        _max = sum(self.weights)

        result = _max

        while _min <= _max:
            _mid = (_min + _max) // 2
            _days = self.days_per_capacity(_mid)
            if _days <= days:
                result = min(result, _mid)
                _max = _mid-1
            else:
                _min = _mid+1

        print(result)

        return result


def test():
    assert Solution().ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert Solution().ship_within_days([3, 2, 2, 4, 1, 4], 3) == 6
    assert Solution().ship_within_days([1, 2, 3, 1, 1], 4) == 3
