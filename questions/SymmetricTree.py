from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = True

        def comapare_node(left, right):

            if not left and not right:
                return True
            if left and right:

                if left.val != right.val:
                    return False
                if comapare_node(left.left, right.right) is False:
                    return False
                if comapare_node(left.right, right.left) is False:
                    return False
                return True

            return False

        result = comapare_node(root.left, root.right)

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

    assert Solution().level_order(tree) is False
    assert Solution().level_order(tree_1) is True
    assert Solution().level_order(tree_2) is False
