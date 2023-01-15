from typing import Optional
from services.Structures import ListNode


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            if head in lst:
                return head
            else:
                lst.append(head)
            head = head.next
        return None


def test():
    pass
