"""
给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。

全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
0 <= i < j < n
nums[i] > nums[j]

局部倒置 的数目等于满足下述条件的下标 i 的数目：
0 <= i < n - 1
nums[i] > nums[i + 1]

当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [1,0,2]
输出：true
解释：有 1 个全局倒置，和 1 个局部倒置。

示例 2：
输入：nums = [1,2,0]
输出：false
解释：有 2 个全局倒置，和 1 个局部倒置。
 
提示：
n == nums.length
1 <= n <= 10^5
0 <= nums[i] < n
nums 中的所有整数 互不相同
nums 是范围 [0, n - 1] 内所有数字组成的一个排列

"""

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        min_num = nums[0]
        max_num = nums[0]
        for i in range(2, n):
            if max_num > nums[i]:
                return False
            min_num = min(min_num, nums[i - 1])
            max_num = max(max_num, nums[i - 1])
        return True


        # 方法二：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        min_suf = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i - 1] > min_suf:
                return False
            min_suf = min(min_suf, nums[i])
        return True


        # 方法三：数学
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        return all(abs(x - i) <= 1 for i, x in enumerate(nums))




