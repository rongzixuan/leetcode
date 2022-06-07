"""
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:


        # 方法一：二分法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            return 0 if nums[0] >= nums[1] else 1

        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left)
            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    left = mid + 1
            elif mid == n-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    right = mid - 1
            else:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] < nums[mid+1]:
                    left = mid + 1
                elif nums[mid] < nums[mid-1]:
                    right = mid - 1


