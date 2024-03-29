"""
有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。

"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(m*k),其中m为flights的长度
        # 空间复杂度：O(n*k)
        dp = [[float('inf')] * (n) for _ in range(k+2)]
        dp[0][src] = 0

        for m in range(1, k+2):
            for i, j, cost in flights:
                dp[m][j] = min(dp[m][j], dp[m-1][i] + cost)
                #print(dp[m][j])

        print(dp)
        min_dist = min(dp[m][dst] for m in range(1, k+2))
        return min_dist if min_dist != float('inf') else -1

    
    
    
    
