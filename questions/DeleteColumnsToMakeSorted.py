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


def test():
    assert Solution().min_deletion_size(["cba", "daf", "ghi"]) == 1
    assert Solution().min_deletion_size(["a", "b"]) == 0
    assert Solution().min_deletion_size(["zyx", "wvu", "tsr"]) == 3
