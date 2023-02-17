from typing import List


class Solution:
    def final_value_after_operations(self, operations: List[str]) -> int:

        hash = {"X++": 1, "++X": 1, "--X": -1, "X--": -1}

        result = 0

        for i in operations:
            result = result + hash[i]

        return result


def test():
    assert Solution().final_value_after_operations(["X++", "++X", "--X", "X--"]) == 0
