"""
最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：

Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
Paste（粘贴）：粘贴 上一次 复制的字符。

给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。

"""

class Solution:
    def minSteps(self, n: int) -> int:

        # 方法一：动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = i
            for j in range(2, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)

        return dp[n]


        # 方法二：动态规划
        # 时间复杂度：O(n * n ** 1/2)
        # 空间复杂度：O(n)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = i
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
                    dp[i] = min(dp[i], dp[i//j] + j)

        return dp[n]


        # 方法三：质因数分解
        # 时间复杂度：O(n ** 1/2)
        # 空间复杂度：O(1)
        res = 0
        tmp = n

        i = 2
        while i * i <= n:
            #print(i)
            while tmp % i == 0:
                #print(i)
                res += i
                tmp //= i
            i += 1

        #print(tmp)
        if tmp > 1:
            res += tmp
        return res

        

