from typing import List


class Solution:
    def truncate_sentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])

def test():
    assert Solution().truncate_sentence("ab c a bc", 3) == "ab c a"

