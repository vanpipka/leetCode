from typing import Optional
from services.Structures import TreeNode


class Solution:

    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 is None and root2 is None:
            return root1

        result = TreeNode()

        def merge_trees_rec(current_node, root_1, root_2):

            if root_1 is None:
                current_node.val = root_2.val
                current_node.left = root_2.left
                current_node.right = root_2.right

                return

            if root_2 is None:
                current_node.val = root_1.val
                current_node.left = root_1.left
                current_node.right = root_1.right

                return

            current_node.val = root_1.val + root_2.val

            if root_1.left is not None or\
                    root_2.left is not None:
                current_node.left = TreeNode()
                merge_trees_rec(current_node.left, root_1.left, root_2.left)

            if root_1.right is not None or \
                    root_2.right is not None:
                current_node.right = TreeNode()
                merge_trees_rec(current_node.right, root_1.right, root_2.right)

        merge_trees_rec(result, root1, root2)

        return result


def test():
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(5)

    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right.right = TreeNode(7)

    Solution().merge_trees(tree, tree_1)
