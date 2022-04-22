"""
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:


        # 方法一：迭代
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        if n <= 0:
            return False
        elif n == 1:
            return True

        while n > 1:
            if n % 2 == 1:
                return False
            n //= 2

        return True


        # 方法二：位运算
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        if n <= 0:
            return False
        elif n == 1:
            return True

        return True if (n & (n-1)) == 0 else False

        






