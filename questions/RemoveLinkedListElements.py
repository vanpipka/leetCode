from typing import Optional
from services.Structures import ListNode


class Solution:
    def remove_elements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        result = None
        prev = None
        while head:

            if head.val == val:
                if not prev:
                    head = head.next
                    continue
                prev.next = head.next
            else:
                prev = head
            head = head.next

            if not result and prev:
                result = prev

        return True
        return result


def test():
    assert Solution().remove_elements(ListNode.create_new_list([1, 2, 3, 6, 4, 5, 6]), 6) is True
    assert Solution().remove_elements(ListNode.create_new_list([1, 1, 1, 6, 4, 5, 6]), 1) is True
    assert Solution().remove_elements(ListNode.create_new_list([1, 2, 2, 1]), 2) is True
