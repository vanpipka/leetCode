from typing import Optional
from services.Structures import TreeNode


class Solution:
    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root

        def set_next(root_1):

            if not root_1 or root_1.left is None:
                return

            root_1.left.next = root_1.right

            if root_1.next and root_1.right:
                root_1.right.next = root_1.next.left

            set_next(root_1.left)
            set_next(root_1.right)

        set_next(root)

        return root
