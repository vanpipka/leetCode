class Solution:
    def character_replacement(self, s: str, k: int) -> int:

        fr_dct = {}
        max_fr, result, start = 0, 0, 0

        for i in range(len(s)):
            fr_dct[s[i]] = fr_dct.get(s[i], 0) + 1

            max_fr = max(max_fr, fr_dct[s[i]])
            is_valid = (i + 1 - start - max_fr <= k)
            if not is_valid:
                fr_dct[s[start]] -= 1
                start += 1

            result = i + 1 - start

        return result


def test():
    assert Solution().character_replacement("ABAB", 2) == 4
    assert Solution().character_replacement("AABABBA", 1) == 4
