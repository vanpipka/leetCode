from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def set_next(node):
            if not node:
                return
            result.append(node.val)
            if node.left:
                set_next(node.left)
            if node.right:
                set_next(node.right)

        set_next(root)

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

    assert Solution().preorder_traversal(tree) == [1, 3, 5, 2]
    assert Solution().preorder_traversal(tree_1) == [2, 1, 4, 3, 7]
