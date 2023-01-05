from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0
        y = len(numbers)-1

        while True:
            sum = numbers[x] + numbers[y]
            if sum == target:
                break
            elif sum > target:
                y -= 1
            else:
                x += 1

            if x == y:
                break

        return [x+1, y+1]


def test():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
