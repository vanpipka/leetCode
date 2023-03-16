from collections import deque
from typing import Optional, List
from services.Structures import TreeNode

class Solution:
    def build_tree(self, inorder, postorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def dfs(start, end):
            if start > end:
                return None
            root = TreeNode(postorder.pop())
            root_index = inorder_map[root.val]
            root.right = dfs(root_index + 1, end)
            root.left = dfs(start, root_index - 1)
            return root

        return dfs(0, len(inorder) - 1)


def test():

    assert Solution().build_tree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
