"""
一个正整数如果能被 a 或 b 整除，那么它是神奇的。
给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。

示例 1：
输入：n = 1, a = 2, b = 3
输出：2

示例 2：
输入：n = 4, a = 2, b = 3
输出：6
 
提示：
1 <= n <= 10^9
2 <= a, b <= 4 * 10^4

"""

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:


        # 方法一：数学（容斥原理） + 二分查找
        # 时间复杂度：O(log(min(a, b)))
        # 空间复杂度：O(1)
        MOD = 10 ** 9 + 7
        left, right = min(a, b), n * min(a, b)
        from math import lcm
        c = lcm(a, b)  # 最小公倍数

        while left <= right:
            mid = left + (right - left) // 2
            #print(left, mid, right)
            count = mid // a + mid // b - mid // c
            #print(count)
            if count == n:
                if mid % a == 0 or mid % b == 0:
                    return mid % MOD
                else:
                    right = mid - 1
            elif count < n:
                left = mid + 1
            else:
                right = mid - 1


        # 方法二：数学（容斥原理） + 二分查找
        # 时间复杂度：O(log(min(a, b)))
        # 空间复杂度：O(1)
        MOD = 10 ** 9 + 7
        c = lcm(a, b)
        m = c // a + c // b - 1
        r = n % m
        res = c * (n // m) % MOD
        if r == 0:
            return res
        addA = a
        addB = b
        for _ in range(r - 1):
            if addA < addB:
                addA += a
            else:
                addB += b
        return (res + min(addA, addB) % MOD) % MOD







