"""
给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。

如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。

示例 1：
输入：a = 12, b = 6
输出：4
解释：12 和 6 的公因子是 1、2、3、6 。

示例 2：
输入：a = 25, b = 30
输出：2
解释：25 和 30 的公因子是 1、5 。
 
提示：
1 <= a, b <= 1000

"""

class Solution:
    def commonFactors(self, a: int, b: int) -> int:


        # 方法一：枚举
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = min(a, b)
        ans = 0
        for i in range(1, n + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans


        # 方法二：枚举优化
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        c, ans = gcd(a, b), 0
        x = 1
        while x * x <= c:
            if c % x == 0:
                ans += 1
                if x * x != c:
                    ans += 1
            x += 1
        return ans






