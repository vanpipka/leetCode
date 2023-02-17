from typing import List


class Solution:
    def restore_string(self, s: str, indices: List[int]) -> str:

        result = [None for _ in range(len(s))]

        for i in range(len(s)):
            result[indices[i]] = s[i]

        return ("").join(result)


def test():
    assert Solution().restore_string("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"

