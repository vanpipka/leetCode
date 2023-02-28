from typing import Optional
from services.Structures import ListNode


class Solution:
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        temp = head
        list_len = 1
        while temp.next:
            list_len += 1
            temp = temp.next  # last elem

        temp.next = head
        count = list_len - (k % list_len)

        while count > 0:
            temp = temp.next
            count -= 1
        result = temp.next
        temp.next = None

        return result


def test():

    node = ListNode.create_new_list([1, 2, 3, 4, 5])
    assert Solution().rotate_right(node, 2)





