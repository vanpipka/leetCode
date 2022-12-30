from typing import Optional
from services.Structures import TreeNode


class Solution:

    def max_depth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        l_length = 1
        r_length = 1

        if root.left is not None:
            l_length += Solution.max_depth(self, root.left)

        if root.right is not None:
            r_length += Solution.max_depth(self, root.right)

        return max(l_length, r_length)
