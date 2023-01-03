# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return None

        length = 0
        temp = head

        while temp is not None:
            length += 1
            temp = temp.next

        length = length - n

        if length == 0:
            temp = head.next
            head.next = None
            del head
            return temp

        curr = head
        prev = None

        while length > 0:
            prev = curr
            curr = curr.next
            length -= 1

        prev.next = curr.next
        curr.next = None
        del curr
        return head
