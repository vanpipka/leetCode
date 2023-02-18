from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def sum_even_grandparent(self, root: TreeNode) -> TreeNode:

        if not root:
            return 0

        summ = 0

        def inorder(node, is_even_valued_p, is_even_valued_g):

            if node:

                nonlocal summ

                if is_even_valued_g:
                    summ += node.val

                inorder(node.left, node.val % 2 == 0, is_even_valued_p)
                inorder(node.right, node.val % 2 == 0, is_even_valued_p)

        inorder(root, False, False)

        return summ


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

    assert Solution().sum_even_grandparent(tree) == 3
    assert Solution().sum_even_grandparent(tree_1) == 11
