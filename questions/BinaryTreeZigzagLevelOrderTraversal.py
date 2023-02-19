from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        def inorder(node, level):

            if node:
                if len(result) <= level:
                    result.append([node.val])
                else:
                    result[level].append(node.val)

                inorder(node.left, level + 1)
                inorder(node.right, level + 1)

        inorder(root, 0)

        return [list(reversed(result[i])) if i % 2 else result[i] for i in range(len(result))]


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

    assert Solution().zigzag_level_order(tree) == [[1], [2, 3], [5]]
    assert Solution().zigzag_level_order(tree_1) == [[2], [3, 1], [4, 7]]


