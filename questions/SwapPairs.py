from typing import Optional
from services.Structures import ListNode


class Solution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        result = head.next
        lst = [head]

        while head and head.next:
            lst.append(head.next)
            head = head.next

        prev = None
        for i in range(0, len(lst) - 1, 2):
            print(lst[i].val)
            lst[i].next = lst[i + 1].next
            lst[i + 1].next = lst[i]
            if prev:
                prev.next = lst[i + 1]
            prev = lst[i]

        return result



def test():

    node = ListNode.create_new_list([1, 2, 3, 4, 5])
    assert Solution().swap_pairs(node)





