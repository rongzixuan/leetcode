"""
给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

示例 1：
输入：n = 3
输出：0
解释：3! = 6 ，不含尾随 0

示例 2：
输入：n = 5
输出：1
解释：5! = 120 ，有一个尾随 0

示例 3：
输入：n = 0
输出：0
 
提示：
0 <= n <= 10^4

进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？

"""


class Solution:
    def trailingZeroes(self, n: int) -> int:


        # 方法一：数学
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        count_2, count_5 = 0, 0 
        for i in range(2, n + 1):
            while i % 2 == 0:
                count_2 += 1
                i //= 2
            while i % 5 == 0:
                count_5 += 1
                i //= 5

        return min(count_2, count_5)


        # 方法二：数学2
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        count = 0
        while n:
            count += (n // 5)
            n //= 5

        return count

  
