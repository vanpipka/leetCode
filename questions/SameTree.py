from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    result = True
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def compare(node_1, node_2):

            if not self.result:
                return
            if not node_1 and not node_2:
                return
            if (not node_1 and node_2) or (node_1 and not node_2):
                self.result = False
                return
            if node_1.val != node_2.val:
                self.result = False
                return
            compare(node_1.left, node_2.left)
            compare(node_1.right, node_2.right)

        compare(p, q)

        return self.result


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

    assert Solution().is_same_tree(tree, tree) is True
    assert Solution().is_same_tree(tree_1, tree) is False
