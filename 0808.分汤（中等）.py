"""
有 A 和 B 两种类型 的汤。一开始每种类型的汤有 n 毫升。有四种分配操作：
提供 100ml 的 汤A 和 0ml 的 汤B 。
提供 75ml 的 汤A 和 25ml 的 汤B 。
提供 50ml 的 汤A 和 50ml 的 汤B 。
提供 25ml 的 汤A 和 75ml 的 汤B 。

当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为 0.25 的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。

注意 不存在先分配 100 ml 汤B 的操作。

需要返回的值： 汤A 先分配完的概率 +  汤A和汤B 同时分配完的概率 / 2。返回值在正确答案 10-5 的范围内将被认为是正确的。

示例 1:
输入: n = 50
输出: 0.62500
解释:如果我们选择前两个操作，A 首先将变为空。
对于第三个操作，A 和 B 会同时变为空。
对于第四个操作，B 首先将变为空。
所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.25 *(1 + 1 + 0.5 + 0)= 0.625。

示例 2:
输入: n = 100
输出: 0.71875
 
提示:
0 <= n <= 10^9

"""

class Solution:
    def soupServings(self, n: int) -> float:


        # 方法一：记忆化搜索
        # 时间复杂度：O()
        # 空间复杂度：O(MAX^2)
        MAX = 5000
        if n > MAX:
            return 1

        #ans = 0
        @cache
        def dfs(a, b):
            #nonlocal ans
            res = 0
            # 第一种情况
            if a > 100 and b > 0:
                res += dfs(a - 100, b) * 0.25
            elif a <= 100 and b <= 0:
                res += 0.25 * 0.5 
            elif a <= 100 and b > 0:
                #print('1:', a, b, p)
                res += 0.25 

            # 第二种情况
            if a > 75 and b > 25:
                res += dfs(a - 75, b - 25) * 0.25
            elif a <= 75 and b <= 25:
                #print('21:', a, b, p)
                res += 0.25 * 0.5
            elif a <= 75:
                #print('22:', a, b, p)
                res += 0.25

            # 第三种情况
            if a > 50 and b > 50:
                res += dfs(a - 50, b - 50) * 0.25
            elif a <= 50 and b <= 50:
                #print('31:', a, b, p)
                res += 0.25 * 0.5
            elif a <= 50:
                #print('32:', a, b, p)
                res +=  0.25

            # 第四种情况
            if a > 25 and b > 75:
                res += dfs(a - 25, b - 75) * 0.25
            elif a <= 25 and b <= 75:
                #print('41:', a, b, p)
                res += 0.25 * 0.5
            elif a <= 25:
                #print('42:', a, b, p)
                res += 0.25
            return res

        return dfs(n, n)
        #return ans


        # 方法二：记忆化搜索
        # 时间复杂度：O(MAX^2)
        # 空间复杂度：O(MAX^2)
        n = (n + 24) // 25
        if n >= 179:
            return 1.0
        @cache
        def dfs(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return (dfs(a - 4, b) + dfs(a - 3, b - 1) +
                    dfs(a - 2, b - 2) + dfs(a - 1, b - 3)) / 4
        return dfs(n, n)


        # 方法三：动态规划
        # 时间复杂度：O(MAX^2)
        # 空间复杂度：O(MAX^2)
        MAX = 5000
        if n > MAX:
            return 1

        n = (n + 24) // 25
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5
        for i in range(1, n + 1):
        #    dp[i][0] = 1
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] += (dp[max(0, i - 4)][j] 
                + dp[max(0, i - 3)][max(0, j - 1)] 
                + dp[max(0, i - 2)][max(0, j - 2)] 
                + dp[max(0, i - 1)][max(0, j - 3)]) / 4
        return dp[n][n]




