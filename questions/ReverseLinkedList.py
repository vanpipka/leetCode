from typing import Optional
from services.Structures import ListNode


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        A = head
        B = head.next

        while A.next:
            if not B:
                break
            C = B.next
            B.next = A
            A = B
            B = C

        head.next = None

        return True
        return A


def test():
    assert Solution().reverse_list(ListNode.create_new_list([1, 2, 3, 4, 5])) is True





