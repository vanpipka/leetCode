from services.Structures import ListNode


class Solution:
    def delete_node(self, node):

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

        return True


def test():

    node = ListNode.create_new_list([1, 2, 3, 4, 5])
    assert Solution().delete_node(node.next.next) is True





