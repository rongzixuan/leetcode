"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。

"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        # 方法一：二分法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        n = len(nums)

        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return right + 1



