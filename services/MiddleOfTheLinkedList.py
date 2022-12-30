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


