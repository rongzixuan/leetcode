"""
给你一个整数数组 nums 。你需要选择 恰好 一个下标（下标从 0 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。

比方说，如果 nums = [6,1,7,4,1] ，那么：
选择删除下标 1 ，剩下的数组为 nums = [6,7,4,1] 。
选择删除下标 2 ，剩下的数组为 nums = [6,1,4,1] 。
选择删除下标 4 ，剩下的数组为 nums = [6,1,7,4] 。

如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 平衡数组 。

请你返回删除操作后，剩下的数组 nums 是 平衡数组 的 方案数 。

示例 1：
输入：nums = [2,1,6,4]
输出：1
解释：
删除下标 0 ：[1,6,4] -> 偶数元素下标为：1 + 4 = 5 。奇数元素下标为：6 。不平衡。
删除下标 1 ：[2,6,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：6 。平衡。
删除下标 2 ：[2,1,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：1 。不平衡。
删除下标 3 ：[2,1,6] -> 偶数元素下标为：2 + 6 = 8 。奇数元素下标为：1 。不平衡。
只有一种让剩余数组成为平衡数组的方案。

示例 2：
输入：nums = [1,1,1]
输出：3
解释：你可以删除任意元素，剩余数组都是平衡数组。

示例 3：
输入：nums = [1,2,3]
输出：0
解释：不管删除哪个元素，剩下数组都不是平衡数组。
 
提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4

"""

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:


        # 方法一：前缀和 + 模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        total = sum(nums)
        total_odd = sum([nums[i] for i in range(1, n, 2)])
        total_even = sum([nums[i] for i in range(0, n, 2)])
        #print(total, total_odd, total_even)

        ans = 0
        pre_total_odd, pre_total_even = 0, 0
        for i in range(n):
            if i % 2 == 0:
                tmp_total_even = (pre_total_even + total_odd - pre_total_odd)
                tmp_total_odd = (pre_total_odd + total_even - pre_total_even - nums[i])
                pre_total_even += nums[i]
            else:
                tmp_total_even = (pre_total_even + total_odd - pre_total_odd - nums[i])
                tmp_total_odd = (pre_total_odd + total_even - pre_total_even)
                pre_total_odd += nums[i]
            #print(tmp_total_odd, tmp_total_even)
            if tmp_total_even == tmp_total_odd:
                ans += 1
        return ans







