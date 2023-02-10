"""
有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。

不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。

现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。

假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。

示例 1：
输入：n = 2, rollMax = [1,1,2,2,2,3]
输出：34
解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。

示例 2：
输入：n = 2, rollMax = [1,1,1,1,1,1]
输出：30

示例 3：
输入：n = 3, rollMax = [1,1,1,2,2,3]
输出：181
 
提示：
1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15

"""

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n * max(rollmax) * C * C)
        # 空间复杂度：O(n * max(rollmax) * C )
        # C = 6
        MOD = 10**9 + 7
        limit = max(rollMax)
        dp = [[[0] * (limit + 1) for _ in range(6)] for _ in range(n + 1)]
        #print(dp)
        for j in range(6):
            dp[1][j][1] = 1
        
        for i in range(2, n + 1):
            for j in range(6):
                for k in range(6):
                    for p in range(1, rollMax[k] + 1):
                        if j != k:
                            dp[i][j][1] += dp[i - 1][k][p]
                        elif p + 1 <= rollMax[j]:
                            dp[i][j][p + 1] += dp[i - 1][k][p]
        #print(dp)

        ans = 0
        for j in range(6):
            for k in range(1, limit + 1):
                ans += dp[n][j][k]
        return ans % MOD


        # 方法二：记忆化搜索
        # 时间复杂度：O(n * max(rollmax) * C * C)
        # 空间复杂度：O(n * max(rollmax) * C )
        # C = 6
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i: int, last: int, left: int) -> int:
            if i == 0: return 1
            res = 0
            for j, mx in enumerate(rollMax):
                if j != last: res += dfs(i - 1, j, mx - 1)
                elif left: res += dfs(i - 1, j, left - 1)
            return res % MOD
        return sum(dfs(n - 1, j, mx - 1) for j, mx in enumerate(rollMax)) % MOD



        
