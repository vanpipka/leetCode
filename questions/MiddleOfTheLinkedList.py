from typing import Optional
from services.Structures import ListNode


class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        length = 0
        temp = head

        while temp is not None:
            length += 1
            temp = temp.next

        length = length//2

        while length > 0:
            length -= 1
            head = head.next

        return head.val


def test():
    assert Solution().middle_node(ListNode.create_new_list([1, 2, 3, 4, 5])) == 3
    assert Solution().middle_node(ListNode.create_new_list([1, 2, 3, 4, 5, 6, 7])) == 4
    assert Solution().middle_node(ListNode.create_new_list([1, 2, 3])) == 2
