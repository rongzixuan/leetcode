"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:


        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        tmp_sum = 0
        n = len(nums)
        if n == 1:
            return nums

        new_nums = []
        for i in range(n):
            tmp_sum += nums[i]
            new_nums.append(tmp_sum)
        return new_nums


        # 方法二：原地修改
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1:
            return nums

        for i in range(1, n):
            nums[i] += nums[i-1]
        return nums


