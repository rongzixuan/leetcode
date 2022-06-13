"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

"""

class Solution:
    def rob(self, nums: List[int]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        dp = [0] * (n+1)
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i])

        #print(dp)
        return dp[n]


        # 方法二：动态规划2
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        dp = [0] * 2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            tmp = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = tmp
            print(dp)

        #print(dp)
        return dp[1]
    
    
