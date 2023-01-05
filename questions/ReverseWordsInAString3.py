from typing import List


class Solution:

    def reverse_words(self, s: str) -> str:

        res = []

        for i in s.split(" "):
            res.append("".join(reversed(list(i))))

        return " ".join(res)


def test():
    assert Solution().reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert Solution().reverse_words("God Ding") == "doG gniD"