
from services.BinarySearch import Solution as BinarySearch
from services.RomanToInteger import Solution as RomanToInteger
from services.LongestCommonPrefix import Solution as LongestCommonPrefix
from services.MergeTwoSortedLists import Solution as MergeTwoSortedLists
from services.SearchInsertPosition import Solution as SearchInsertPosition

if __name__ == '__main__':

    # https://leetcode.com/problems/binary-search/
    BinarySearch = BinarySearch()
    assert BinarySearch.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert BinarySearch.search([-1, 0, 3, 5, 9, 12], 2) == -1

    # https://leetcode.com/problems/roman-to-integer/
    # RomanToInteger = RomanToInteger()
    # assert RomanToInteger.roman_to_int('III') == 3
    # assert RomanToInteger.roman_to_int('LVIII') == 58
    # assert RomanToInteger.roman_to_int('MCMXCIV') == 1994

    # https://leetcode.com/problems/longest-common-prefix/
    # LongestCommonPrefix = LongestCommonPrefix()
    # assert LongestCommonPrefix.longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    # assert LongestCommonPrefix.longest_common_prefix(["dog", "racecar", "car"]) == ""
    # assert LongestCommonPrefix.longest_common_prefix(["cir", "car"]) == "c"

    # https://leetcode.com/problems/merge-two-sorted-lists/
    # MergeTwoSortedLists = MergeTwoSortedLists()
    # assert MergeTwoSortedLists.merge_two_lists(list1=[1, 2, 4], list2=[1, 3, 4]) == [1, 1, 2, 3, 4, 4]
    # assert MergeTwoSortedLists.merge_two_lists(list1=[1, 10, 12], list2=[1, 3, 4]) == [1, 1, 3, 4, 10, 12]
    # assert MergeTwoSortedLists.merge_two_lists(list1=[], list2=[0]) == [0]
    # assert MergeTwoSortedLists.merge_two_lists(list1=[], list2=[]) == []

    # https://leetcode.com/problems/search-insert-position/
    # SearchInsertPosition = SearchInsertPosition()
    # assert SearchInsertPosition.search_insert(nums=[1, 3, 5, 6], target=5) == 2
    # assert SearchInsertPosition.search_insert(nums=[1, 3, 5, 6], target=2) == 1
    # assert SearchInsertPosition.search_insert(nums=[1, 3, 5, 6], target=7) == 4

    pass
