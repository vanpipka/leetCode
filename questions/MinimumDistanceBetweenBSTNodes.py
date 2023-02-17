from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def min_diff_in_bst(self, root: Optional[TreeNode]) -> List[int]:

        minimum = float("inf")
        result = []

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        inorder(root)

        for i in range(1, len(result)):
            minimum = min(minimum, result[i]-result[i-1])

        return minimum


def test():

    tree = TreeNode(90)
    tree.left = TreeNode(69)
    tree.left.left = TreeNode(49)
    tree.left.right = TreeNode(89)
    tree.left.left.right = TreeNode(52)

    assert Solution().min_diff_in_bst(tree) == 1

