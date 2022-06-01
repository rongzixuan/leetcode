"""
你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。
你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。

如果你能使这个正方形，则返回 true ，否则返回 false 。

示例 1:
输入: matchsticks = [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。

示例 2:
输入: matchsticks = [3,3,3,3,4]
输出: false
解释: 不能用所有火柴拼成一个正方形。

提示:
1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8

"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:


        # 方法一：回溯
        # 时间复杂度：O(4^n)
        # 空间复杂度：O(n)
        n = len(matchsticks)
        if n < 4:
            return False

        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        length = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > length:
            return False

        egdes = [0] * 4

        def dfs(index):
            if egdes == [length] * 4:
                return True
            for i in range(4):
                if egdes[i] + matchsticks[index] <= length:
                    egdes[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    egdes[i] -= matchsticks[index]
            return False

        return dfs(0)


        # 方法二：状压压缩 + 动态规划
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(2^n)
        n = len(matchsticks)
        if n < 4:
            return False

        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        length = total // 4

        dp = [-1] * (1 << n)
        dp[0] = 0

        for i in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if i & (1 << k) == 0:
                    continue
                j = i & ~(1 << k)
                #print(i, j)
                #print('dp[i] before:', dp[i])
                if dp[j] >= 0 and dp[j] + v <= length:
                    dp[i] = (dp[j] + v) % length
                    break
                #print('dp[i] after:', dp[i])

        return dp[-1] == 0


