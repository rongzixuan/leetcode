"""
给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。

"""

class Solution:
    def getSum(self, a: int, b: int) -> int:


        # 方法一：位运算
        # 时间复杂度：O(log(max_n))
        # 空间复杂度：O(1)
        MASK1 = 4294967296   # 2 ^ 32
        MASK2 = 2147483648   # 2 ^ 31
        MASK3 = 2147483647   # 2 ^ 31 - 1

        #print(a, b)
        #print(a & b)
        a %= MASK1
        b %= MASK1
        #print(a, b)
        #print(a & b)

        while b != 0:
            tmp = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = tmp

        if a & MASK2: # 负数
            return ~ a ^ MASK2 ^ MASK3
        else:
            return a
        
        
        
