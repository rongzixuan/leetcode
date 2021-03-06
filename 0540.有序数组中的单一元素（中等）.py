"""
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

示例 1:
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: nums =  [3,3,7,7,10,11,11]
输出: 10
 
提示:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:


        # 方法一：二分法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            #print(left, mid, right)
            if mid == 0 or mid == n - 1:
                return nums[mid]
            elif nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif right - mid == 1:
                if nums[right] != nums[mid]:
                    return nums[right]
                elif nums[mid] != nums[left]:
                    return nums[left]
            elif (right - mid) % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    right = mid
                else:
                    left = mid
            elif (right - mid) % 2 == 1:
                if nums[mid] == nums[mid - 1]:              
                    left = mid + 1
                else:
                    right = mid - 1


        # 方法二：二分法2
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        n = len(nums)
        left, right = 0, n - 1
        while left < right:            
            mid = left + (right - left) // 2
            #print(left, mid, right)
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid

        return nums[right]




