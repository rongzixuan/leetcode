"""
给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：
子数组的长度是 k，且
子数组中的所有元素 各不相同 。

返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。
子数组 是数组中一段连续非空的元素序列。

示例 1：
输入：nums = [1,5,4,2,9,9,9], k = 3
输出：15
解释：nums 中长度为 3 的子数组是：
- [1,5,4] 满足全部条件，和为 10 。
- [5,4,2] 满足全部条件，和为 11 。
- [4,2,9] 满足全部条件，和为 15 。
- [2,9,9] 不满足全部条件，因为元素 9 出现重复。
- [9,9,9] 不满足全部条件，因为元素 9 出现重复。
因为 15 是满足全部条件的所有子数组中的最大子数组和，所以返回 15 。

示例 2：
输入：nums = [4,4,4], k = 3
输出：0
解释：nums 中长度为 3 的子数组是：
- [4,4,4] 不满足全部条件，因为元素 4 出现重复。
因为不存在满足全部条件的子数组，所以返回 0 。
 
提示：
1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5

"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        
        # 方法一：滑动窗口 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        nums = [0] * (k - 1) + nums
        #print(nums)
        ans = 0
        tmp_ans = 0
        count = defaultdict(int)
        for i in range(k - 1, n + k - 1):
            #print(nums[i], nums[i - k])
            if i == k - 1:
                tmp_ans = nums[i]
                count[nums[i]] += 1
            else:                         
                if i - k >= k - 1:
                    #print('i - k:', i - k)
                    tmp_ans -= nums[i - k]
                    if nums[i - k] in count:
                        count[nums[i - k]] -= 1
                        if count[nums[i - k]] == 0:
                            del count[nums[i - k]]
                tmp_ans += nums[i]
                count[nums[i]] += 1
            if len(count) == k:
                ans = max(ans, tmp_ans)
        return ans
        
        
        
