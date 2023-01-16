from typing import Optional, List
from services.Structures import TreeNode


class Solution:

    def lowest_common_ancestor(self, root: Optional[TreeNode], p, q) -> List[int]:

        # for depth level
        while True:
            if root.val > p and root.val > q:
                root = root.left
            elif root.val < p and root.val < q:
                root = root.right
            else:
                return root.val

        # for min value ancestor
        """
        if not root:
            return root
        lst_r, lst_l = [], []
        result = root.val

        def search(node, val, lst):

            if not node:
                return
            if node.val == val:
                lst.append(node.val)
                return
            if node.val > val:
                lst.append(node.val)
                search(node.left, val, lst)
            else:
                lst.append(node.val)
                search(node.right, val, lst)

        search(root, p, lst_l)
        search(root, q, lst_r)

        for i in range(min(len(lst_l), len(lst_r))):
            if lst_r[i] != lst_l[i]:
                break
            result = min(result, lst_l[i])

        return result
        """

def test():
    tree = TreeNode(6)
    tree.left = TreeNode(2)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(4)
    tree.left.right.left = TreeNode(3)
    tree.left.right.right = TreeNode(5)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)

    assert Solution().lowest_common_ancestor(tree, 3, 5) == 4
    assert Solution().lowest_common_ancestor(tree, 2, 8) == 6
    assert Solution().lowest_common_ancestor(tree, 2, 4) == 2
