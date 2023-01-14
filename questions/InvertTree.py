from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        result = root

        def invert_node(node):

            if not node:
                return

            node.left, node.right = node.right, node.left
            invert_node(node.left)
            invert_node(node.right)

        invert_node(root)

        return result


def test():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.right = TreeNode(5)

    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(2)
    tree_1.left.left = TreeNode(4)
    tree_1.left.right = TreeNode(3)
    tree_1.right.left = TreeNode(3)
    tree_1.right.right = TreeNode(4)

    tree_2 = TreeNode(2)
    tree_2.left = TreeNode(3)
    tree_2.right = TreeNode(3)
    tree_2.left.left = TreeNode(4)
    tree_2.left.right = TreeNode(5)
    tree_2.right.left = TreeNode(5)
    tree_2.right.right = TreeNode(4)
    tree_2.left.right.left = TreeNode(8)
    tree_2.left.right.right = TreeNode(9)
    tree_2.right.right.left = TreeNode(9)
    tree_2.right.right.right = TreeNode(8)

    assert Solution().invert_tree(tree) is False
    assert Solution().invert_tree(tree_1) is True
    assert Solution().invert_tree(tree_2) is False
