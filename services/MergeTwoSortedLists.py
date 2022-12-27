from typing import Optional


# Definition for singly-linked lists
class Solution:
    def merge_two_lists(self, list1: Optional[list], list2: Optional[list]) -> Optional[list]:

        if not len(list1):
            return list2

        if not len(list2):
            return list1

        pos_list1: int = 0
        pos_list2: int = 0

        result: list = []

        for i in range(len(list1)+len(list2)-1):

            if pos_list1 == len(list1) or pos_list2 == len(list2):
                break

            if list1[pos_list1] < list2[pos_list2]:
                result.append(list1[pos_list1])
                pos_list1 += 1

            else:
                result.append(list2[pos_list2])
                pos_list2 += 1

        if pos_list1 < len(list1):
            result += list1[pos_list1:]

        if pos_list2 < len(list2):
            result += list2[pos_list2:]

        return result
