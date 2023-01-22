# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from services.Structures import ListNode


class Solution:
    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmp = result = head

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        for i in sorted(lst):
            tmp.val = i
            tmp = tmp.next

        return result

def test():
    node = ListNode.create_new_list([1, 3, 2, 4, 5])
    assert Solution().sort_list(node) == [1, 2, 3, 4, 5]