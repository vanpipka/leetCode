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
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @staticmethod
    def create_new_list(structure: dict):

        pass

    def pre_order(self):
        if not self:
            return

        print(self.val)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()


class NTreeNode:
    def __init__(self, val=0):
        self.val: int = val
        self.children: List[NTreeNode] = []

    @staticmethod
    def create_new_list(structure: dict):

        pass
