"""
给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos 处。在一步移动中，你可以向左或者向右移动一个位置。
给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 109 + 7 取余 的结果。
如果所执行移动的顺序不完全相同，则认为两种方法不同。

注意：数轴包含负整数。

示例 1：
输入：startPos = 1, endPos = 2, k = 3
输出：3
解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法：
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
可以证明不存在其他方法，所以返回 3 。

示例 2：
输入：startPos = 2, endPos = 5, k = 10
输出：0
解释：不存在从 2 到 5 且恰好移动 10 步的方法。
 
提示：
1 <= startPos, endPos, k <= 1000

"""

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        
        # 方法一：回溯（超时）
        # 时间复杂度：
        # 空间复杂度：
        if abs(endPos - startPos) == k and k > 0:
            return 1
        
        ans = 0
        def dfs(index, step):
            #print(index, step)
            nonlocal ans
            if index == endPos and step == k:
                ans += 1
                
            for i in [-1, 1]:
                if step + 1 <= k:
                    dfs(index + i, step + 1)
        
        dfs(startPos, 0)
        return ans % (10**9+7)


        # 方法二：记忆化搜索
        # 时间复杂度：
        # 空间复杂度：
        if abs(endPos - startPos) == k and k > 0:
            return 1
        
        ans = 0
        MOD = (10**9+7)
        @cache
        def dfs(index, step):
            #print(index, step)
            nonlocal ans
            res = 0
            if index == endPos and step == k:
                #ans += 1
                res += 1
                
            for i in [-1, 1]:
                if step + 1 <= k:
                    res += dfs(index + i, step + 1)
            return res % MOD
        
        return dfs(startPos, 0)
        #return ans % (10**9+7)


        # 方法三：记忆化搜索
        # 时间复杂度：
        # 空间复杂度：
        if abs(endPos - startPos) == k and k > 0:
            return 1
        
        ans = 0
        MOD = (10**9+7)
        @lru_cache(None)
        def dfs(index, step):
            #print(index, step)
            nonlocal ans
            res = 0
            if index == endPos and step == k:
                #ans += 1
                res += 1
                
            for i in [-1, 1]:
                if step + 1 <= k:
                    res += dfs(index + i, step + 1)
            return res % MOD
        
        return dfs(startPos, 0)
        #return ans % (10**9+7)


        # 方法四：数学（排列组合） + 动态规划
        # 时间复杂度：
        # 空间复杂度：
        # 利用组合的递推公式
        if abs(endPos - startPos) == k and k > 0:
            return 1
        elif abs(endPos - startPos) > k:
            return 0

        MOD = 10 ** 9 + 7
        k2 = k - endPos + startPos
        if k2 % 2 != 0:
            return 0
        k1 = (k - endPos + startPos) // 2
        dp = [[0] * (k + 1) for _ in range(k + 1)]
        dp[0][0] = 1

        for i in range(1, k + 1):
            dp[i][0] = 1
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        #print(dp)

        return dp[k][k1] % MOD
        
        
        
        
