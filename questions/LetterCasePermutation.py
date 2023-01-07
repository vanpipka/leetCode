from typing import List


class Solution:

    def letter_case_permutation(self, s: str) -> List[str]:

        result = []
        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                result.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)

        backtrack()

        print(result)
        return result


def test():
    #assert Solution().letter_case_permutation("Jw") == ['jW', 'jw', 'JW', 'Jw']
    #assert Solution().letter_case_permutation("po") == ['PO', 'po', 'pO', 'Po']
    #assert Solution().letter_case_permutation("a1b2") == ['A1B2', 'a1b2', 'A1b2', 'a1B2']
    #assert Solution().letter_case_permutation("3z4") == ["3Z4", "3z4"]
    assert Solution().letter_case_permutation("abcd") == ["3Z4", "3z4"]
    assert Solution().letter_case_permutation("C") == ["C", "c"]
