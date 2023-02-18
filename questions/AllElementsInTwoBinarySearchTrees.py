from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def get_all_elements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        result = []

        def set_next(node):
            if not node:
                return
            result.append(node.val)
            set_next(node.left)
            set_next(node.right)

        set_next(root1)
        set_next(root2)

        print(sorted(result))

        return sorted(result)


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

    assert Solution().get_all_elements(tree, tree_1) == [1, 1, 2, 2, 3, 3, 4, 5, 7]