from typing import Optional, List
from services.Structures import NTreeNode


class Solution:
    def preorder_traversal(self, root: Optional[NTreeNode]) -> List[int]:

        result = []

        def set_next(node):
            if not node:
                return

            result.append(node.val)

            for i in node.children:
                set_next(i)

        set_next(root)

        return result


def test():
    tree = NTreeNode(1)
    tree.children.append(NTreeNode(2))
    tree.children.append(NTreeNode(3))
    tree.children.append(NTreeNode(4))

    assert Solution().preorder_traversal(tree) == [1, 2, 3, 4]
