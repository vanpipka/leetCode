from typing import List


class Solution:
    def find_anagrams(self, s: str, p: str) -> List[int]:

        sorted_p = sorted(p)
        len_p = len(p)
        result = []

        for i in range(len(s)-(len_p-1)):
            if sorted(s[i:i+len_p]) == sorted_p:
                result.append(i)

        return result


def test():
    assert Solution().find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert Solution().find_anagrams("abab", "ab") == [0, 1, 2]

