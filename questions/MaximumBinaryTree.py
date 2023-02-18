from typing import Optional, List
from services.Structures import TreeNode


class Solution:
    def construct_maximum_binary_tree(self, nums: List[int]) -> Optional[TreeNode]:

        def create(nums):
            if not nums:
                return
            max_el = max(nums)
            ind_max = nums.index(max_el)
            root = TreeNode(max_el)

            root.left = create(nums[:ind_max])
            root.right = create(nums[ind_max+1:])

            return root

        result = create(nums)

        return result
def test():


    assert Solution().construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])

