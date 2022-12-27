from services.RomanToInteger import Solution as RomanToInteger
from services.LongestCommonPrefix import Solution as LongestCommonPrefix

if __name__ == '__main__':

    # https://leetcode.com/problems/roman-to-integer/
    RomanToInteger = RomanToInteger()
    assert RomanToInteger.roman_to_int('III') == 3
    assert RomanToInteger.roman_to_int('LVIII') == 58
    assert RomanToInteger.roman_to_int('MCMXCIV') == 1994

    # https://leetcode.com/problems/longest-common-prefix/
    LongestCommonPrefix = LongestCommonPrefix()
    assert LongestCommonPrefix.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert LongestCommonPrefix.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert LongestCommonPrefix.longestCommonPrefix(["cir", "car"]) == "c"

    pass
