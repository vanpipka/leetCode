import collections
from operator import attrgetter
from typing import List


class Solution:
    def top_k_frequent(self, words: List[str], k: int) -> List[str]:

        s_dict = {val[0]: val[1] for val in sorted(collections.Counter(words).items(), key=lambda x: (-x[1], x[0]))}

        return [i for i, j in s_dict.items()][:k]


def test():
    assert Solution().top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], 3) == ["i", "love", "coding"]
    assert Solution().top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
    assert Solution().top_k_frequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) \
           == ["the", "is", "sunny", "day"]

