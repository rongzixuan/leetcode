"""
给你一个整数数组 nums 和两个整数 minK 以及 maxK 。

nums 的定界子数组是满足下述条件的一个子数组：
子数组中的 最小值 等于 minK 。
子数组中的 最大值 等于 maxK 。

返回定界子数组的数目。
子数组是数组中的一个连续部分。

示例 1：
输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5
输出：2
解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。

示例 2：
输入：nums = [1,1,1,1], minK = 1, maxK = 1
输出：10
解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。
 
提示：
2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6

"""

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        
        # 方法一：双指针（超时）
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        n = len(nums)
        ans = 0
        
        left = 0
        #min_flag, max_flag = False, False
        min_count, max_count = 0, 0
        for right in range(n):
            if nums[right] > maxK or nums[right] < minK:
                left, min_count, max_count = right + 1, 0, 0
                continue
            if nums[right] == minK:
                min_count += 1
            if nums[right] == maxK:
                max_count += 1
                
            if min_count > 0 and max_count > 0:
                #print('left, right:', left, right)
                index = left
                tmp_min_count, tmp_max_count = min_count, max_count
                while index <= right and tmp_min_count > 0  and tmp_max_count > 0:
                    #print('left, right, tmp_min_count, tmp_max_count:', left, right, tmp_min_count, tmp_max_count)
                    ans += 1                   
                    if index < n and nums[index] == minK:
                        tmp_min_count -= 1
                    if index < n and nums[index] == maxK:
                        tmp_max_count -= 1
                    index += 1
                    
        return ans


        # 方法二：双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        ans = 0
        left = 0
        index1, index2 = -1, -1
        for right in range(n):
            if nums[right] > maxK or nums[right] < minK:
                left = right + 1
                continue
            if nums[right] == minK:
                index1 = right
            if nums[right] == maxK:
                index2 = right
            ans += max(0, min(index1, index2) - left + 1)
        return ans




