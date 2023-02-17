from typing import List


class Solution:
    def most_words_found(self, sentences: List[str]) -> int:

        result = float("-inf")

        for i in sentences:
            result = max(result, len(i.split(" ")))

        return result


def test():
    assert Solution().most_words_found(["alice and bob love leetcode",
                                        "i think so too",
                                        "this is great thanks very much"]) == 6
