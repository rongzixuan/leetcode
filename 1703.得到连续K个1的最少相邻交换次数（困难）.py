"""
给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。

请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。

示例 1：
输入：nums = [1,0,0,1,0,1], k = 2
输出：1
解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。

示例 2：
输入：nums = [1,0,0,0,0,0,1,1], k = 3
输出：5
解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。

示例 3：
输入：nums = [1,1,0,1], k = 2
输出：0
解释：nums 已经有连续 2 个 1 了。

提示：
1 <= nums.length <= 10^5
nums[i] 要么是 0 ，要么是 1 。
1 <= k <= sum(nums)

"""

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:


        # 方法一：前缀和 + 贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        """count = [q - i for i, q in enumerate(i for i, x in enumerate(nums) if x)]
        pre = list(accumulate(count, initial=0))  # p 的前缀和
        print('count:', count)
        print('pre:', pre)
        return min(pre[i] + pre[i + k] - pre[i + k // 2] * 2 - count[i + k // 2] * (k % 2)
                   for i in range(len(count) - k + 1)) """


        g, preSum = [], [0]
        for i, num in enumerate(nums):
            if num == 1:
                g.append(i - len(g))
                preSum.append(preSum[-1] + g[-1])  # g的前缀和
        #print('g:', g)
        #print('preSum:', preSum)
        m, res = len(g), inf
        for i in range(m - k + 1):
            mid = i + k // 2
            r = g[mid]
            res = min(res, (1 - k % 2) * r + (preSum[i + k] - preSum[mid + 1]) - (preSum[mid] - preSum[i]))
        return res





