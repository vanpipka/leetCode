from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def path_sum(self, root: Optional[TreeNode], targetSum: int) -> List[int]:

        def next(node, summ):

            if not node:
                return False

            summ -= node.val

            if not node.left and not node.right:
                return summ == 0

            return next(node.left, summ) or next(node.right, summ)

        result = next(root, targetSum)

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

    #assert Solution().path_sum(tree, 4) is False
    assert Solution().path_sum(tree_1, 7) is True
