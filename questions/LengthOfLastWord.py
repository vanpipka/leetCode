class Solution:
    def length_of_last_word(self, s: str) -> int:

        return len([x for x in s.split(" ") if x][-1])


def test():
    assert Solution().length_of_last_word("   fly me   to   the moon  ") == 4
    assert Solution().length_of_last_word("luffy is still joyboy") == 6
