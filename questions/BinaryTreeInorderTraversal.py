from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def inorder(node):

            if node:

                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        inorder(root)

        return result


def test():
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(5)

    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right.right = TreeNode(7)

    assert Solution().inorder_traversal(tree) == [5, 3, 1, 2]
    assert Solution().inorder_traversal(tree_1) == [1, 4, 2, 3, 7]
