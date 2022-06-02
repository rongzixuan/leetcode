"""
给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。 

示例 1:
输入: n = 5
输出: 2
解释: 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。

示例 2:
输入: n = 9
输出: 3
解释: 9 = 4 + 5 = 2 + 3 + 4

示例 3:
输入: n = 15
输出: 4
解释: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
 
提示:
1 <= n <= 10^9

"""

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:


        # 方法一：数学
        # 时间复杂度：O(n**0.5)
        # 空间复杂度：O(1)
        if n == 1:
            return 1

        count = 0
        for i in range(1, n + 1):   # i为连续元素的个数
            if (1 + i) * i // 2 > n:
                break
            if i % 2 == 1:
                if n % i == 0:
                    print(i)
                    count += 1
            else:
                if (n / i) - (n // i) == 0.5:
                    print(i)
                    count += 1        

        return count


        # 方法二：数学
        # 时间复杂度：O(n**0.5)
        # 空间复杂度：O(1)
        def isKConsecutive(n: int, k: int) -> bool:
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if isKConsecutive(n, k):
                ans += 1
            k += 1
        return ans

      
      
