class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:

        s_array = s.split(" ")
        pattern_array = [i for i in pattern]

        if len(s_array) != len(pattern_array):
            return False

        if len(list(set(s_array))) != len(list(set(pattern_array))):
            return False

        pattern_dict = {}

        for i in range(len(pattern_array)):

            val = pattern_dict.get(pattern_array[i])

            if val is None:
                pattern_dict[pattern_array[i]] = s_array[i]
                continue

            if val != s_array[i]:
                return False

        return True


def test():
    assert Solution().word_pattern(pattern="abba", s="dog cat cat dog") is True
    assert Solution().word_pattern(pattern="abba", s="dog cat cat fish") is False
    assert Solution().word_pattern(pattern="aaaa", s="dog cat cat dog") is False
    assert Solution().word_pattern(pattern="abba", s="dog dog dog dog") is False
