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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def create_new_list(structure: dict):

        pass
