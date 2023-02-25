from typing import List


class Solution:
    def num_decodings(self, s: str) -> int:

        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        result = [1]

        for i in range(1, len(s)+1):
            result.append(0)
            last = int(s[i-1])
            if last > 0:
                result[i] += result[i-1]
            if i > 1:
                if s[i-2] != "0" and int(s[i-2:i]) < 27:
                    result[i] += result[i-2]

        return result[-1]


def test():
    assert Solution().num_decodings("27") == 1
    assert Solution().num_decodings("10") == 1
    assert Solution().num_decodings("121314") == 10
    assert Solution().num_decodings("12") == 2
    assert Solution().num_decodings("106715234") == 4
    assert Solution().num_decodings("226") == 3
    assert Solution().num_decodings("06") == 0
