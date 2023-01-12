from typing import Optional
from services.Structures import ListNode


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        result = head
        prev = head
        head = head.next

        while head:

            if prev.val == head.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return True
        return result


def test():
    assert Solution().delete_duplicates(ListNode.create_new_list([1, 2, 3, 3, 4, 5, 6])) is True
    assert Solution().delete_duplicates(ListNode.create_new_list([1, 1, 1, 2, 4, 5, 6])) is True
    assert Solution().delete_duplicates(ListNode.create_new_list([1, 2, 3])) is True
