from typing import Optional
from services.Structures import TreeNode


class Solution:
    def sum_numbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        result = 0

        def dfs(node, lst):
            nonlocal result

            if not node:
                return

            lst.append(str(node.val))

            if not node.left and not node.right:
                result += int(("").join(lst))
                return

            len_lst = len(lst)
            dfs(node.left, lst)
            dfs(node.right, lst[:len_lst])

        dfs(root, [])

        print(result)

        return result


def test():

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.right = TreeNode(5)

    tree_1 = TreeNode(3)
    tree_1.left = TreeNode(9)
    tree_1.right = TreeNode(20)
    tree_1.right.left = TreeNode(15)
    tree_1.right.right = TreeNode(7)

    assert Solution().sum_numbers(tree) == 259
    assert Solution().sum_numbers(tree_1) == 35261
