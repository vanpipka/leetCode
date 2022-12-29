from services.FirstBadVersion import Solution as FirstBadVersion
from services.RemoveNthNodeFromEndOfList import Solution as RemoveNthNodeFromEndOfList
from services.MiddleOfTheLinkedList import Solution as MiddleOfTheLinkedList
from services.LinkedNode import ListNode
from services.RotateArray import Solution as RotateArray
from services.ReverseWordsInAString3 import Solution as ReverseWordsInAString3
from services.MoveZeroes import Solution as MoveZeroes
from services.ReverseString import Solution as ReverseString
from services.TwoSum2InputArrayIsSorted import Solution as TwoSum2InputArrayIsSorted
from services.SquaresOfASortedArray import Solution as SquaresOfASortedArray
from services.BinarySearch import Solution as BinarySearch
from services.RomanToInteger import Solution as RomanToInteger
from services.LongestCommonPrefix import Solution as LongestCommonPrefix
from services.MergeTwoSortedLists import Solution as MergeTwoSortedLists
from services.SearchInsertPosition import Solution as SearchInsertPosition


if __name__ == '__main__':

    # https://leetcode.com/problems/middle-of-the-linked-list/
    # MiddleOfTheLinkedList = MiddleOfTheLinkedList()
    # assert MiddleOfTheLinkedList.middle_node(ListNode.create_new_list([1, 2, 3, 4, 5])) == 3
    # assert MiddleOfTheLinkedList.middle_node(ListNode.create_new_list([1, 2, 3, 4, 5, 6, 7])) == 4
    # assert MiddleOfTheLinkedList.middle_node(ListNode.create_new_list([1, 2, 3])) == 2


    # https://leetcode.com/problems/remove-nth-node-from-end-of-list
    # RemoveNthNodeFromEndOfList = RemoveNthNodeFromEndOfList()

    # https://leetcode.com/problems/reverse-words-in-a-string-iii/
    # ReverseWordsInAString3 = ReverseWordsInAString3()
    # assert ReverseWordsInAString3.reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    # assert ReverseWordsInAString3.reverse_words("God Ding") == "doG gniD"

    # https://leetcode.com/problems/reverse-string/
    # ReverseString = ReverseString()
    # assert ReverseString.reverse_string(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    # assert ReverseString.reverse_string(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]

    # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    # TwoSum2InputArrayIsSorted = TwoSum2InputArrayIsSorted()
    # assert TwoSum2InputArrayIsSorted.twoSum([2, 7, 11, 15], 9) == [1, 2]
    # assert TwoSum2InputArrayIsSorted.twoSum([2, 3, 4], 6) == [1, 3]
    # assert TwoSum2InputArrayIsSorted.twoSum([-1, 0], -1) == [1, 2]

    # https://leetcode.com/problems/move-zeroes/
    # MoveZeroes = MoveZeroes()
    # assert MoveZeroes.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    # assert MoveZeroes.moveZeroes([0]) == [0]

    #https://leetcode.com/problems/rotate-array/
    # RotateArray = RotateArray()
    # assert RotateArray.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    # assert RotateArray.rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]

    # https://leetcode.com/problems/squares-of-a-sorted-array/
    # SquaresOfASortedArray = SquaresOfASortedArray()
    # assert SquaresOfASortedArray.sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    # assert SquaresOfASortedArray.sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

    # https://leetcode.com/problems/first-bad-version/
    # FirstBadVersion = FirstBadVersion()
    # assert FirstBadVersion.first_bad_version(5) == 0

    # https://leetcode.com/problems/binary-search/
    # BinarySearch = BinarySearch()
    # assert BinarySearch.search([-1, 0, 3, 5, 9, 12], 9) == 4
    # assert BinarySearch.search([-1, 0, 3, 5, 9, 12], 2) == -1

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
