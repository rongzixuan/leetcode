"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:


        # 方法一：数学模拟
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        if n <= 0:
            return False
        elif n == 1:
            return True

        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3

        return True

    
        # 方法二：数学
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        # 1162261467 = 3 ^ 19
        return n > 0 and 1162261467 % n == 0


    
    
