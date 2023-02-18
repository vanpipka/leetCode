from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def bst_from_preorder(self, preorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        root = TreeNode(preorder[0])
        center = 1

        while center < len(preorder) and preorder[center] < root.val:
            center += 1

        root.left = self.bst_from_preorder(preorder[1:center])
        root.right = self.bst_from_preorder(preorder[center:])

        return root


def test():

    dd = Solution().bst_from_preorder([3, 1, 2])
    assert Solution().bst_from_preorder([4, 2])
    assert Solution().bst_from_preorder([8, 5, 1, 7, 10, 12])
