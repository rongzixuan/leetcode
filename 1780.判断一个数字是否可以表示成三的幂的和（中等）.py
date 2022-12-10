"""
给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。
对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。

示例 1：
输入：n = 12
输出：true
解释：12 = 31 + 32

示例 2：
输入：n = 91
输出：true
解释：91 = 30 + 32 + 34

示例 3：
输入：n = 21
输出：false
 
提示：
1 <= n <= 10^7

"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:


        # 方法一：三进制
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        while n:
            a = n % 3
            if a != 1 and a != 0:
                return False
            n //= 3
        return True 




