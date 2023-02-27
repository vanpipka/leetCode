from typing import List


class Solution:
    def min_moves_to_seat(self, seats: List[int], students: List[int]) -> int:

        seats.sort()
        students.sort()

        count = 0

        for i in range(len(seats)):
            count += abs(seats[i]-students[i])

        return count


def test():
    assert Solution().min_moves_to_seat([3, 1, 5], [2, 7, 4]) == 4



