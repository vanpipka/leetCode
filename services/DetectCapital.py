class Solution:
    def detect_capital_use(self, word: str) -> bool:

        if word == word.upper():
            return True
        if word == word.capitalize():
            return True
        if word == word.lower():
            return True

        return False

