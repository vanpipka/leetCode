from typing import Optional
from services.Structures import TreeNode


class Solution:

    def max_depth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        l_length = 1
        r_length = 1

        if root.left is not None:
            l_length += Solution.max_depth(self, root.left)

        if root.right is not None:
            r_length += Solution.max_depth(self, root.right)

        return max(l_length, r_length)


def test():
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(20)
    tree.right.right = TreeNode(7)
    tree.right.right.left = TreeNode(1)
    tree.right.right.left.right = TreeNode(1)
    tree_1 = TreeNode(3)
    tree_1.right = TreeNode(20)

    assert Solution().max_depth(tree) == 5
    assert Solution().max_depth(tree_1) == 2
