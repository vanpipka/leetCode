from typing import Optional
from services.Structures import ListNode


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            if head in lst:
                return True
            else:
                lst.append(head)
            head = head.next
        return False


def test():
    pass
