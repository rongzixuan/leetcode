"""
给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。

请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。

示例 1：
输入：nums = [3,6,1,0]
输出：1
解释：6 是最大的整数，对于数组中的其他整数，6 大于数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。

示例 2：
输入：nums = [1,2,3,4]
输出：-1
解释：4 没有超过 3 的两倍大，所以返回 -1 。

示例 3：
输入：nums = [1]
输出：0
解释：因为不存在其他数字，所以认为现有数字 1 至少是其他数字的两倍。

提示：
1 <= nums.length <= 50
0 <= nums[i] <= 100
nums 中的最大元素是唯一的

"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:


        # 方法一：遍历模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1:
            return 0

        max_num, less_num = float('-inf'), float('-inf')
        index = -1

        for i, num in enumerate(nums):
            if num > max_num:
                less_num = max_num
                max_num = num
                index = i
            elif max_num >= num and num > less_num:
                less_num = num

        if max_num >= 2 * less_num:
            return index
        return -1



