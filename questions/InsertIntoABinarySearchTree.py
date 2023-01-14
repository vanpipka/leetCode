from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def insert_into_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        result = root

        def insert(node):

            if not node:
                return
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left)
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right)

        insert(root)

        return result


def test():

    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)

    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right.right = TreeNode(7)

    Solution().insert_into_BST(tree, 5)

