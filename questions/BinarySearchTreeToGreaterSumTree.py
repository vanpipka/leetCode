from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def bst_to_gst(self, root: TreeNode) -> TreeNode:

        result = []
        sum = 0
        def inorder(node):
            nonlocal sum
            if node:
                inorder(node.right)
                node.val += sum
                sum = node.val
                result.append(node.val)
                inorder(node.left)

        inorder(root)

        return result


def test():
    tree = TreeNode(6)
    tree.left = TreeNode(4)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(3)

    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right.right = TreeNode(7)

    assert Solution().bst_to_gst(tree) == [5, 3, 1, 2]
    assert Solution().bst_to_gst(tree_1) == [1, 4, 2, 3, 7]
