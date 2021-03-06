"""
给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10^n 。
 
示例 1：
输入：n = 2
输出：91
解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。 

示例 2：
输入：n = 0
输出：1

提示：
0 <= n <= 8

"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:


        # 方法一：数学（排列组合）
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        ans = 0
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            ans += 10
            tmp_ans = 9
            for i in range(1, n):
                tmp_ans *= (10 - i)
                ans += tmp_ans
                #print(i, tmp_ans)
                
        return ans


        # 方法二：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n == 2:
            return 91

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 10
        dp[2] = 81
        for i in range(3, n + 1):
            print('i:', i)
            dp[i] = dp[i - 1] * (11 - i)

        #print('dp:', dp)
        return sum(dp[i] for i in range(1, n + 1))

    
