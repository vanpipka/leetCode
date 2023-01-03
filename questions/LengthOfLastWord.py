class Solution:
    def length_of_last_word(self, s: str) -> int:

        return len([x for x in s.split(" ") if x][-1])
