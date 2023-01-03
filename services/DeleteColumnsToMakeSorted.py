from typing import List


class Solution:
    def min_deletion_size(self, strs: List[str]) -> int:

        result = 0

        if len(strs) == 0:
            return result

        for i in range(len(strs[0])):
            curr_str = ""

            for x in strs:
                curr_str += x[i]

            if curr_str != "".join(sorted(curr_str)):
                result += 1

        return result
