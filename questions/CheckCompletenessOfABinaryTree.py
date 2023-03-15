from collections import deque
from typing import Optional, List
from services.Structures import TreeNode

class Solution:
    def is_complete_tree(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        queue.append(root)
        while queue[0] is not None:
            node = queue.popleft()
            queue.append(node.left)
            queue.append(node.right)
        while queue and queue[0] is None:
            queue.popleft()
        return not queue


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

    assert Solution().is_complete_tree(tree) is True
    assert Solution().is_complete_tree(tree_1) is False
