from typing import List


class Solution:
    def count_matches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        position = {"color": 1, "type": 0, "name": 2}.get(ruleKey)
        result = 0
        for i in items:
            if i[position] == ruleValue:
                result += 1

        return result
def test():
    assert Solution().count_matches([["phone","blue","pixel"],
                                     ["computer","silver","lenovo"],
                                     ["phone","gold","iphone"]], "color", "silver") == 1

