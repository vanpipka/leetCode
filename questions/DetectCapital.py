class Solution:
    def detect_capital_use(self, word: str) -> bool:

        if word == word.upper():
            return True
        if word == word.capitalize():
            return True
        if word == word.lower():
            return True

        return False


def test():
    assert Solution().detect_capital_use("g") is True
    assert Solution().detect_capital_use("USA") is True
    assert Solution().detect_capital_use("leetcode") is True
    assert Solution().detect_capital_use("Google") is True
