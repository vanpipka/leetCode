from typing import Optional, List
from services.Structures import ListNode


# Definition for singly-linked lists
class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        result = ListNode()

        def append_to_head(head):

            _min = float("inf")
            for i in lists:
                if not i:
                    continue
                _min = min(_min, i.val)

            if _min == float("inf"):
                return

            for node in lists:
                if not node or node.val != _min:
                    continue

                lists[lists.index(node)] = node.next
                head.next = ListNode()
                head.next.val = _min
                head = head.next

            append_to_head(head)

        append_to_head(result)

        return result.next

def test():
    assert Solution().merge_k_lists([ListNode.create_new_list([1, 4, 5]),
                                  ListNode.create_new_list([1, 3, 4]),
                                  ListNode.create_new_list([2, 6])]) == 3

