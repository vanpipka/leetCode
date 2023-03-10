from random import random
from typing import Optional
from services.Structures import ListNode


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        lst = []
        temp = self.head
        while temp:
            lst.append(temp)
            temp = temp.next

        return random.choice(lst).val


def test():
    pass