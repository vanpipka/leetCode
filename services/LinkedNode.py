from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_new_list(list: List[int]):

        node = None
        next_element = None
        for i in reversed(list):
            node = ListNode(i, next_element)
            next_element = node

        return node
