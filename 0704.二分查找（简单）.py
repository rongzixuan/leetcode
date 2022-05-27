"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 方法一：二分法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            #print(left, right)
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return -1
