from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        result_list = []

        for pos in range(len(strs[0])):
            breaked: bool = False
            for word in strs[1:]:
                if len(word) <= pos:
                    breaked = True
                    break
                if word[pos] != strs[0][pos]:
                    breaked = True
                    break

            if breaked:
                break

            result_list.append(strs[0][pos])

        return ''.join(result_list)
