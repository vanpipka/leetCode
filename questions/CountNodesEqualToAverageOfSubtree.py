from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def average_of_subtree(self, root: TreeNode) -> TreeNode:

        if not root:
            return 0

        summ = 0

        def inorder(node):
            nonlocal summ
            if node:

                if not node.left and not node.right:
                    summ += 1
                    return 1, node.val

                r_w = inorder(node.right)
                l_w = inorder(node.left)

                if (node.val + l_w[1] + r_w[1]) // (l_w[0] + r_w[0] + 1) == node.val:
                    summ += 1

                return l_w[0] + r_w[0] +1, l_w[1] + r_w[1] + node.val

            else:
                return 0, 0

        inorder(root)

        print(summ)

        return summ


def test():

    tree = TreeNode(4)
    tree.left = TreeNode(8)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(1)
    tree.right.right = TreeNode(6)

    assert Solution().average_of_subtree(tree) == 5

