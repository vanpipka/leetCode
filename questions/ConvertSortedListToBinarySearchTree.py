from random import random
from typing import Optional
from services.Structures import ListNode, TreeNode


class Solution:

    def sorted_list_to_bst(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        lst = []

        while head:
            lst.append(head)
            head = head.next

        def add_node(arr):

            if not arr:
                return

            mid = len(arr)//2

            node = TreeNode(arr[mid].val)

            node.left = add_node(arr[:mid])
            node.right = add_node(arr[mid+1:])

            return node

        result = add_node(lst)
        return result


def test():
    tree = Solution().sorted_list_to_bst(ListNode.create_new_list([-10, -3, 0, 5, 9]))
    tree.pre_order()
