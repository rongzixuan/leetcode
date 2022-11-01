"""
给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。
子数组 是数组中 连续 的一部分。 

示例 1：
输入：nums = [1], k = 1
输出：1

示例 2：
输入：nums = [1,2], k = 4
输出：-1

示例 3：
输入：nums = [2,-1,2], k = 3
输出：3
 
提示：
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
1 <= k <= 10^9

"""

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:


        # 方法一：前缀和 + 单调双端队列
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            if nums[i] >= k:
                return 1
            preSum[i + 1] = nums[i] + preSum[i]

        queue = deque()
        ans = n + 1
        for i, pre in enumerate(preSum):
            while queue and pre - preSum[queue[0]] >= k:
                ans = min(ans, i - queue.popleft())
            while queue and preSum[queue[-1]] >= pre:
                queue.pop()
            queue.append(i)
        return ans if ans <= n else -1



