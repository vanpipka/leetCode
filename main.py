from services.Structures import ListNode, TreeNode
from questions.FirstBadVersion import Solution as FirstBadVersion
from questions.RemoveNthNodeFromEndOfList import Solution as RemoveNthNodeFromEndOfList
from questions.MiddleOfTheLinkedList import Solution as MiddleOfTheLinkedList
from questions.AddTwoNumbers import Solution as AddTwoNumbers
from questions.LengthOfLongestSubstring import Solution as LengthOfLongestSubstring
from questions.MaximumDepthOfBinaryTree import Solution as MaximumDepthOfBinaryTree
from questions.RotateArray import Solution as RotateArray
from questions.ReverseWordsInAString3 import Solution as ReverseWordsInAString3
from questions.MoveZeroes import Solution as MoveZeroes
from questions.ReverseString import Solution as ReverseString
from questions.TwoSum2InputArrayIsSorted import Solution as TwoSum2InputArrayIsSorted
from questions.SquaresOfASortedArray import Solution as SquaresOfASortedArray
from questions.BinarySearch import Solution as BinarySearch
from questions.RomanToInteger import Solution as RomanToInteger
from questions.LongestCommonPrefix import Solution as LongestCommonPrefix
from questions.MergeTwoSortedLists import Solution as MergeTwoSortedLists
from questions.SearchInsertPosition import Solution as SearchInsertPosition
from questions.DayOfTheYear import Solution as DayOfTheYear
from questions.ValidParentheses import Solution as ValidParentheses
from questions.PermutationInString import Solution as PermutationInString
from questions.LengthOfLastWord import Solution as LengthOfLastWord
from questions.PlusOne import Solution as PlusOne
from questions.ReverseInteger import Solution as ReverseInteger
from questions.StringToIntegerAtoi import Solution as StringToIntegerAtoi
from questions.FloodFill import Solution as FloodFill
from questions.MaxAreaOfIsland import Solution as MaxAreaOfIsland
from questions.WaterBottles import Solution as WaterBottles
from questions.MergeTwoBinaryTrees import Solution as MergeTwoBinaryTrees
from questions.WordPattern import Solution as WordPattern
from questions.DetectCapital import Solution as DetectCapital
from questions.DeleteColumnsToMakeSorted import Solution as DeleteColumnsToMakeSorted
from questions.WordSearch import Solution as WordSearch
from questions.PopulatingNextRightPointersInEachNode import Solution as PopulatingNextRightPointersInEachNode
from questions.Matrix01 import Solution as Matrix01
from questions.RottingOranges import Solution as RottingOranges

if __name__ == '__main__':

    # https://leetcode.com/problems/rotting-oranges/
    RottingOranges = RottingOranges()
    assert RottingOranges.oranges_rotting([[0]]) == 0
    assert RottingOranges.oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert RottingOranges.oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert RottingOranges.oranges_rotting([[0, 2]]) == 0

    # https://leetcode.com/problems/01-matrix/
    # Matrix01 = Matrix01()
    # assert Matrix01.update_matrix([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]) == [[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
    # assert Matrix01.update_matrix([[1, 0, 1, 1], [1, 1, 1, 1], [0, 0, 1, 1], [1, 0, 1, 1]]) == [[1, 0, 1, 2], [1, 1, 2, 3], [0, 0, 1, 2], [1, 0, 1, 2]]
    # assert Matrix01.update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # assert Matrix01.update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

    # https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    # PopulatingNextRightPointersInEachNode = PopulatingNextRightPointersInEachNode()
    # tree_1 = TreeNode(1)
    # tree_1.left = TreeNode(2)
    # tree_1.right = TreeNode(3)
    # tree_1.left.left = TreeNode(4)
    # tree_1.left.right = TreeNode(5)
    # tree_1.right.left = TreeNode(6)
    # tree_1.right.right = TreeNode(7)
    # PopulatingNextRightPointersInEachNode.connect(tree_1)

    # https://leetcode.com/problems/word-search/
    # WordSearch = WordSearch()
    # assert WordSearch.exist(board=[["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
    #  ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]],
    #                         word="AAAAAAAAAAAAAAa") is False
    # assert WordSearch.exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], word="ABCESEEEFS") is True
    # assert WordSearch.exist(board=[["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], word="AAB") is True
    # assert WordSearch.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED") is True
    # assert WordSearch.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE") is True
    # assert WordSearch.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB") is False

    # https://leetcode.com/problems/delete-columns-to-make-sorted/
    # DeleteColumnsToMakeSorted = DeleteColumnsToMakeSorted()
    # assert DeleteColumnsToMakeSorted.min_deletion_size(["cba", "daf", "ghi"]) == 1
    # assert DeleteColumnsToMakeSorted.min_deletion_size(["a", "b"]) == 0
    # assert DeleteColumnsToMakeSorted.min_deletion_size(["zyx", "wvu", "tsr"]) == 3

    # https://leetcode.com/problems/detect-capital/
    # DetectCapital = DetectCapital()
    # assert DetectCapital.detect_capital_use("g") is True
    # assert DetectCapital.detect_capital_use("USA") is True
    # assert DetectCapital.detect_capital_use("leetcode") is False
    # assert DetectCapital.detect_capital_use("Google") is True

    # https://leetcode.com/problems/word-pattern/
    # WordPattern = WordPattern()
    # assert WordPattern.word_pattern(pattern="abba", s="dog cat cat dog") is True
    # assert WordPattern.word_pattern(pattern="abba", s="dog cat cat fish") is False
    # assert WordPattern.word_pattern(pattern="aaaa", s="dog cat cat dog") is False
    # assert WordPattern.word_pattern(pattern="abba", s="dog dog dog dog") is False

    # https://leetcode.com/problems/merge-two-binary-trees/
    # MergeTwoBinaryTrees = MergeTwoBinaryTrees()

    # tree = TreeNode(1)
    # tree.left = TreeNode(3)
    # tree.right = TreeNode(2)
    # tree.left.left = TreeNode(5)

    # tree_1 = TreeNode(2)
    # tree_1.left = TreeNode(1)
    # tree_1.left = TreeNode(1)
    # tree_1.right = TreeNode(3)
    # tree_1.left.right = TreeNode(4)
    # tree_1.right.right = TreeNode(7)

    # MergeTwoBinaryTrees.merge_trees(tree, tree_1)

    # https://leetcode.com/problems/water-bottles/
    # WaterBottles = WaterBottles()
    # assert WaterBottles.num_water_bottles(9, 3) == 13
    # assert WaterBottles.num_water_bottles(15, 4) == 19

    # https://leetcode.com/problems/max-area-of-island/
    # MaxAreaOfIsland = MaxAreaOfIsland()
    # assert MaxAreaOfIsland.max_area_of_island([
    #     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
    # assert MaxAreaOfIsland.max_area_of_island([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0

    # https://leetcode.com/problems/flood-fill/
    # FloodFill = FloodFill()
    # assert FloodFill.flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2) \
    #        == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    # assert FloodFill.flood_fill([[0, 0, 0], [0, 0, 0]], sr=1, sc=1, color=0) == [[0, 0, 0], [0, 0, 0]]

    # https://leetcode.com/problems/string-to-integer-atoi/
    # StringToIntegerAtoi = StringToIntegerAtoi()

    # assert StringToIntegerAtoi.my_atoi("+0 123") == 0
    # assert StringToIntegerAtoi.my_atoi("-+12") == 0
    # assert StringToIntegerAtoi.my_atoi("-91283472332") == -2147483648
    # assert StringToIntegerAtoi.my_atoi("   -42") == -42
    # assert StringToIntegerAtoi.my_atoi("4193 with words") == 4193

    # https://leetcode.com/problems/reverse-integer/
    # ReverseInteger = ReverseInteger()
    # assert ReverseInteger.reverse(123) == 321
    # assert ReverseInteger.reverse(-123) == -321
    # assert ReverseInteger.reverse(120) == 21
    # assert ReverseInteger.reverse(900000) == 9

    # https://leetcode.com/problems/plus-one/
    # PlusOne = PlusOne()
    # assert PlusOne.plus_one([1, 2, 3]) == [1, 2, 4]
    # assert PlusOne.plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    # assert PlusOne.plus_one([9]) == [1, 0]

    # https://leetcode.com/problems/length-of-last-word/
    # LengthOfLastWord = LengthOfLastWord()
    # assert LengthOfLastWord.length_of_last_word("   fly me   to   the moon  ") == 4
    # assert LengthOfLastWord.length_of_last_word("luffy is still joyboy") == 6

    # https://leetcode.com/problems/permutation-in-string/
    # PermutationInString = PermutationInString()
    # assert PermutationInString.check_inclusion("ab", "eidbaooo") is True
    # assert PermutationInString.check_inclusion("ab", "ab") is True
    # assert PermutationInString.check_inclusion("ab", "eidboaoo") is not True
    # s1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef"
    # s2 = "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"
    # assert PermutationInString.check_inclusion(s1, s2) is not True

    # https://leetcode.com/problems/valid-parentheses/
    # ValidParentheses = ValidParentheses()
    # assert ValidParentheses.is_valid(']') is False
    # assert ValidParentheses.is_valid('(]') is not True
    # assert ValidParentheses.is_valid('()') is True
    # assert ValidParentheses.is_valid('()[]{}') is True
    # assert ValidParentheses.is_valid('(])') is False

    # https://leetcode.com/problems/day-of-the-year/
    # DayOfTheYear = DayOfTheYear()
    # assert DayOfTheYear.day_of_year("2019-01-09") == 9
    # assert DayOfTheYear.day_of_year("2019-02-10") == 41

    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    # LengthOfLongestSubstring = LengthOfLongestSubstring()
    # assert LengthOfLongestSubstring.length_of_longest_substring("abcabcbb") == 3
    # assert LengthOfLongestSubstring.length_of_longest_substring("bbbbb") == 1
    # assert LengthOfLongestSubstring.length_of_longest_substring("pwwkew") == 3
    # assert LengthOfLongestSubstring.length_of_longest_substring("aab") == 2
    # assert LengthOfLongestSubstring.length_of_longest_substring("dvdf") == 3
    # assert LengthOfLongestSubstring.length_of_longest_substring("au") == 2

    # https://leetcode.com/problems/add-two-numbers/
    # AddTwoNumbers = AddTwoNumbers()
    # assert AddTwoNumbers.add_two_numbers(ListNode.create_new_list([2, 4, 3]), ListNode.create_new_list([5, 6, 4])) == 807
    # assert AddTwoNumbers.add_two_numbers(ListNode.create_new_list([9, 9, 9, 9, 9, 9, 9]),
    #                                     ListNode.create_new_list([9, 9, 9, 9])) == 10009998

    # https://leetcode.com/problems/maximum-depth-of-binary-tree/
    # tree = TreeNode(3)
    # tree.left = TreeNode(9)
    # tree.right = TreeNode(20)
    # tree.right.left = TreeNode(20)
    # tree.right.right = TreeNode(7)
    # tree.right.right.left = TreeNode(1)
    # tree.right.right.left.right = TreeNode(1)
    # tree_1 = TreeNode(3)
    # tree_1.right = TreeNode(20)
    # MaximumDepthOfBinaryTree = MaximumDepthOfBinaryTree()
    # assert MaximumDepthOfBinaryTree.max_depth(tree) == 5
    # assert MaximumDepthOfBinaryTree.max_depth(tree_1) == 2

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
