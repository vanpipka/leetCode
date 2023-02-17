from typing import List


class Solution:
    def balanced_string_split(self, s: str) -> int:
        result = 0
        counter_map = {"R": 0, "L": 0}
        for i in s:
            counter_map[i] = counter_map[i]+1
            if counter_map["R"] == counter_map["L"]:
                result += 1
                counter_map["R"] = 0
                counter_map["L"] = 0

        return result


def test():
    assert Solution().balanced_string_split("RLRRLLRLRL") == 4


