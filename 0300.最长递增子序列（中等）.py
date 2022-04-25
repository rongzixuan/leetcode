"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
            
        n = len(nums)

        # 方法一：动态规划
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        # 返回 dp 数组最大值
        return max(dp)


        # 方法二：动态规划 + 贪心 + 二分
        res = []

        for num in nums:
            if res == [] or num > res[-1]:
                res.append(num)
            else:
                left, right = 0, len(res) - 1
                while left <= right:
    
                    mid = left + (right - left) // 2
                    if res[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                res[left] = num

        #print('res:', res)
        return len(res)

        
