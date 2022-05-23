"""
给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。
以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。
 
示例 1：
输入：nums = [1,2,1,2,6,7,5,1], k = 2
输出：[0,3,5]
解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。

示例 2：
输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
输出：[0,2,4]
 
提示：
1 <= nums.length <= 2 * 10^4
1 <= nums[i] < 2^16
1 <= k <= floor(nums.length / 3)

"""

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:


        # 方法一：前缀和 + 滑动窗口
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        tmp_sum1, tmp_sum2, tmp_sum3 = 0, 0, 0
        max_1, max_12, max_123 = 0, 0, 0
        max_1_index, max_12_index, max_123_index = 0, [], []

        for i in range(2*k, n):
            tmp_sum1 += nums[i - 2 * k]
            tmp_sum2 += nums[i - k]
            tmp_sum3 += nums[i]

            if i >= 3 * k - 1:
                if tmp_sum1 > max_1:
                    max_1 = tmp_sum1
                    max_1_index = i - 3 * k + 1
                if max_1 + tmp_sum2 > max_12:
                    max_12 = max_1 + tmp_sum2
                    max_12_index = [max_1_index, i - 2 * k + 1]
                if max_12 + tmp_sum3 > max_123:
                    max_123 = max_12 + tmp_sum3
                    max_123_index = [max_12_index[0], max_12_index[1], i - k + 1]
                tmp_sum1 -= nums[i - 3 * k + 1]
                tmp_sum2 -= nums[i - 2 * k + 1]
                tmp_sum3 -= nums[i - k + 1]
            
            #print(max_1_index, max_12_index, max_123_index)

        return max_123_index


        # 方法二：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)       

        pre_sum = [0] * (n+1)
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
        #print(pre_sum)

        # dp[i][j]表示以i结尾，有j个子数组的和的最大值
        dp = [[0] * 4 for _ in range(n+1)]
        for i in range(k, n + 1):
            for j in range(1, 4):
                dp[i][j] = max(dp[i-1][j], dp[i-k][j-1] + pre_sum[i] - pre_sum[i-k])
        #print(dp)

        # 找到最大值对应的位置
        index = 3
        i = n
        res = [0] * 3
        while index > 0 and i >= 0:
            while dp[i][index] == dp[i-1][index]:
                i -= 1
            #else:
            index -= 1
            res[index] = i - k               
            i -= k

        return res

        
