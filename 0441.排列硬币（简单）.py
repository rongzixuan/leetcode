"""
你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

"""

class Solution:
    def arrangeCoins(self, n: int) -> int:


        # 方法一：二分法
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        if n < 3:
            return 1

        left, right = 0, 2*n**0.5
        
        while left <= right - 2:
            #print(left, right)
            mid = left + (right - left) // 2
            if ((1 + mid) * mid // 2) == n:
                return int(mid)
            elif ((1 + mid) * mid // 2) > n:
                right = mid
            elif ((1 + mid) * mid // 2) < n:
                left = mid

        return int(left)


        # 方法二：数学
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        return int((pow(8*n+1, 0.5) - 1) // 2)






