from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def find_target(self, root: Optional[TreeNode], k: int) -> List[int]:

        result = []

        def order(node):

            if node:

                order(node.left)
                result.append(node.val)
                order(node.right)

        order(root)

        result.sort()
        left = 0
        right = len(result)-1
        while True:

            if left == right:
                return False

            sum = result[left]+result[right]
            if sum == k:
                return True

            if sum > k:
                right -= 1
            else:
                left += 1

        return False


def test():

    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(-4)
    tree.left.right = TreeNode(1)

    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right.right = TreeNode(7)

    assert Solution().find_target(tree, -1) is True
    assert Solution().find_target(tree_1, 16) is False
