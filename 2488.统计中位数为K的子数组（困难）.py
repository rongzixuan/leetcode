"""
给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。

统计并返回 nums 中的 中位数 等于 k 的非空子数组的数目。

注意：
数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
子数组是数组中的一个连续部分。

示例 1：
输入：nums = [3,2,1,4,5], k = 4
输出：3
解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。

示例 2：
输入：nums = [2,3,1], k = 3
输出：1
解释：[3] 是唯一一个中位数等于 3 的子数组。
 
提示：
n == nums.length
1 <= n <= 10^5
1 <= nums[i], k <= n
nums 中的整数互不相同

"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:


        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        from collections import defaultdict
        n = len(nums)
        #pre = [0]
        count = defaultdict(int)
        ans = 1
        i = nums.index(k)

        total = 0
        for j in range(i + 1, n):
            total = total + (1 if nums[j] > k else -1)
            count[total] += 1
            if total == 0 or total == 1:
                ans += 1

        total = 0
        for j in range(i - 1, -1, -1):
            total += (1 if nums[j] < k else -1)
            if total == 0 or total == -1:
                ans += 1
            if total in count:
                ans += count[total]
            if total + 1 in count:
                ans += count[total + 1]
        return ans




