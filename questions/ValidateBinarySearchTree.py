from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def is_valid_BST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return True

        def is_valid(node, left, right):

            if not node:
                return True

            if not(left < node.val < right):
                return False

            return is_valid(node.left, left, node.val) and is_valid(node.right, node.val, right)

        return is_valid(root, float('-inf'), float('inf'))


def test():

    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)

    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(3)
    tree_1.left.left = TreeNode(4)
    tree_1.left.right = TreeNode(7)

    tree_2 = TreeNode(5)
    tree_2.left = TreeNode(4)
    tree_2.right = TreeNode(6)
    tree_2.right.left = TreeNode(3)
    tree_2.right.right = TreeNode(7)

    tree_3 = TreeNode(2)
    tree_3.left = TreeNode(2)
    tree_3.right = TreeNode(2)

    assert Solution().is_valid_BST(tree) is True
    assert Solution().is_valid_BST(tree_1) is False
    assert Solution().is_valid_BST(tree_2) is False
    assert Solution().is_valid_BST(tree_3) is False
