from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def sorted_array_to_BST(self, nums: List[int]) -> Optional[TreeNode]:

        def make_BST(lst):
            if not lst:
                return None
            mid = len(lst) // 2
            node = TreeNode(lst[mid])
            node.left = make_BST(lst[:mid])
            node.right = make_BST(lst[mid + 1:])
            return node

        node = make_BST(nums)
        return True


def test():

    assert Solution().sorted_array_to_BST([-10, -3, 0, 5, 9]) is True
    assert Solution().sorted_array_to_BST([1, 3]) is True
