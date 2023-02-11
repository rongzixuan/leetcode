"""
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

"""

class Solution:
    def tribonacci(self, n: int) -> int:

        # 方法一：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        dp = [0] * (n+1)
        dp[1] = dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        return dp[n]


        # 方法二：动态规划2
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1

        for i in range(3, n+1):
            a, b, c = b, c, a + b + c

        return c


        # 方法三：矩阵快速幂
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        def matrix_multiply(a: List[List[int]], b: List[List[int]]):
            #print(a)
            m, n, l = len(a), len(b[0]), len(a[0])
            #print('m, n, l:', m, n, l)
            c = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    for k in range(l):
                        c[i][j] += a[i][k] * b[k][j]

            return c

        def matrix_pow(n, a):
            res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

            while n:
                #print('n:', n)
                if n & 1:   # 二进制最后一位判断奇数
                    #print('n:', n)
                    res = matrix_multiply(a, res)
                a = matrix_multiply(a, a)
                n >>= 1

            return res

        a = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        re = matrix_pow(n, a) 
        #print(re)
        return re[0][2]





