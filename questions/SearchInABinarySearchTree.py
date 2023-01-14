from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def search_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node):

            if not node:
                return False
            if node.val == val:
                return node
            left_result = search(node.left)
            if left_result:
                return left_result
            right_result = search(node.right)
            if right_result:
                return right_result

        result = search(root)

        return result is not None


def test():

    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)

    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right.right = TreeNode(7)

    assert Solution().search_BST(tree, 2) is True
    assert Solution().search_BST(tree_1, 5) is False
    assert Solution().search_BST(tree_1, 3) is True
