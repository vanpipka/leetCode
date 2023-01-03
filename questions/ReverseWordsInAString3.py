from typing import List


class Solution:

    def reverse_words(self, s: str) -> str:

        res = []

        for i in s.split(" "):
            res.append("".join(reversed(list(i))))

        return " ".join(res)
