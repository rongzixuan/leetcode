"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 双指针
        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for k in range(j, n):
            nums[k] = 0

        return nums

    
    
