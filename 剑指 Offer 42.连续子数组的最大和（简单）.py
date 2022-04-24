"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

"""

class Status:
    def __init__(self, lSum, rSum, mSum, iSum):
        self.lSum = lSum
        self.rSum = rSum
        self.mSum = mSum
        self.iSum = iSum

class Solution:
    def pushUp(self, lSub, rSub):
        lSum = max(lSub.lSum, lSub.iSum + rSub.lSum)
        rSum = max(lSub.rSum + rSub.iSum, rSub.rSum)
        mSum = max(lSub.mSum, rSub.mSum, lSub.rSum + rSub.lSum)
        iSum = lSub.iSum + rSub.iSum
        return Status(lSum, rSum, mSum, iSum)

    def getInfo(self, nums, left, right):
        if left == right:
            return Status(nums[left], nums[left], nums[left], nums[left])
        mid = (left + right) >> 1
        lSub = self.getInfo(nums, left, mid)
        rSub = self.getInfo(nums, mid+1, right)
        return self.pushUp(lSub, rSub)


    def maxSubArray(self, nums: List[int]) -> int:

        # 方法一：动态规划
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        max_num = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_num = max(max_num, dp[i])

        #print('dp:', dp)
        #print('max_num:', max_num)
        return max_num


        # 方法二：分治
        n = len(nums)
        return self.getInfo(nums, 0, n-1).mSum

    
    
    
