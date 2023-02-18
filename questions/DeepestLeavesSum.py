
from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    max_depth = 0

    def deepest_leaves_sum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        map = {}

        def inorder(node, depth):

            if node:
                if not node.left and not node.right:

                    self.max_depth = max(depth, self.max_depth)
                    lst = map.get(depth, [])
                    lst.append(node.val)
                    map[depth] = lst

                inorder(node.left, depth+1)
                inorder(node.right, depth+1)

        inorder(root, 0)

        return sum(map[self.max_depth])


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

    assert Solution().deepest_leaves_sum(tree) == 5
    assert Solution().deepest_leaves_sum(tree_1) == 11
