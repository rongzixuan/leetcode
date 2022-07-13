"""
给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:


        # 方法一：数学
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        min_num = min(nums)
        count = 0

        for num in nums:
            count += num - min_num
        #print(count)

        return count

    
    
