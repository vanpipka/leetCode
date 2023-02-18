from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []

        def backtrack(st, position):

            if position == len(digits):
                result.append(st)
                return

            for i in map[digits[position]]:
                backtrack(st+i, position+1)

        backtrack("", 0)

        return result


def test():
    assert Solution().letter_combinations("23") == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
