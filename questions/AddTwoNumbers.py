from typing import Optional
from services.Structures import ListNode


class Solution:

    @staticmethod
    def list_node_to_int(list_node: Optional[ListNode]) -> int:
        if not list_node:
            return 0
        result = [str(list_node.val)]
        while list_node.next:
            result.append(str(list_node.next.val))
            list_node = list_node.next

        return "".join(reversed(result))

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = int(self.list_node_to_int(l1))+int(self.list_node_to_int(l2))

        node = None
        next_element = None
        for i in [i for i in str(res)]:
            node = ListNode(int(i), next_element)
            next_element = node

        return res
        return node  # for leet code


def test():
    assert Solution().add_two_numbers(ListNode.create_new_list([2, 4, 3]), ListNode.create_new_list([5, 6, 4])) == 807
    assert Solution().add_two_numbers(ListNode.create_new_list([9, 9, 9, 9, 9, 9, 9]),
                                         ListNode.create_new_list([9, 9, 9, 9])) == 10009998



