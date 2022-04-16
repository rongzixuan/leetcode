"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

 

示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

示例 2：
输入：nums = [0,0,0], target = 1
输出：0
 

提示：
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4

"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:


        # 方法一：排序 + 双指针
        # 时间复杂度：O(nlog + n^2)
        # 空间复杂度：O(logn)
        n = len(nums)
        nums.sort()
        
        res = float('inf')
        for first in range(n - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, n - 1
            while second < third:
                #print('before:', first, second, third)
                if nums[first] + nums[second] + nums[third] == target:
                    #print('True:', first, second, third)
                    return target
                if abs(nums[first] + nums[second] + nums[third] - target) < abs(res - target):
                    res = nums[first] + nums[second] + nums[third]
                if nums[first] + nums[second] + nums[third] > target:
                    third -= 1
                    #while third > second + 1 and nums[third - 1] == nums[third]:
                    #    third -= 1
                elif nums[first] + nums[second] + nums[third] < target:
                    second += 1        
                    #while second < third - 1 and nums[second + 1] == nums[second]:
                    #    second += 1       
                #print('after:', first, second, third)               

        return res


        # 方法二：排序 + 双指针2
        # 时间复杂度：O(nlog + n^2)
        # 空间复杂度：O(logn)
        n = len(nums)
        nums.sort()
        
        res = float('inf')
        for first in range(n - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, n - 1
            while second < third:
                #print('before:', first, second, third)
                if nums[first] + nums[second] + nums[third] == target:
                    #print('True:', first, second, third)
                    return target
                if abs(nums[first] + nums[second] + nums[third] - target) < abs(res - target):
                    res = nums[first] + nums[second] + nums[third]
                if nums[first] + nums[second] + nums[third] > target:
                    tmp_third = third - 1
                    while tmp_third > second + 1 and nums[tmp_third] == nums[third]:
                        tmp_third -= 1
                    third = tmp_third
                elif nums[first] + nums[second] + nums[third] < target:
                    tmp_second = second + 1        
                    while tmp_second < third - 1 and nums[tmp_second] == nums[second]:
                        tmp_second += 1  
                    second = tmp_second     
                #print('after:', first, second, third)               

        return res
    
    
    
    
