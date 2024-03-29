"""
给你一个整数 n 。按下述规则生成一个长度为 n + 1 的数组 nums ：
nums[0] = 0
nums[1] = 1
当 2 <= 2 * i <= n 时，nums[2 * i] = nums[i]
当 2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1]

返回生成数组 nums 中的 最大 值。

"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        # 方法一：模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if n == 0 or n == 1:
            return n

        nums = [0] * (n+1)
        nums[1] = 1
        max_num = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            max_num = max(max_num, nums[i])

        return max_num
        

        
        
        
