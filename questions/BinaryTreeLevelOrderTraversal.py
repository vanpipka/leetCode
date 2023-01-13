from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = [[root.val]]

        def set_next(node, level):

            level += 1

            if not node:
                return
            if len(result)-1 < level and (node.left or node.right):
                result.append([])
            if node.left:
                result[level].append(node.left.val)
            if node.right:
                result[level].append(node.right.val)
            set_next(node.left, level)
            set_next(node.right, level)

        set_next(root, 0)

        print(result)

        return result


def test():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.right = TreeNode(5)

    tree_1 = TreeNode(3)
    tree_1.left = TreeNode(9)
    tree_1.right = TreeNode(20)
    tree_1.right.left = TreeNode(15)
    tree_1.right.right = TreeNode(7)

    assert Solution().level_order(tree) == [[1], [2, 3], [4, 5]]
    assert Solution().level_order(tree_1) == [[3], [9, 20], [15, 7]]
