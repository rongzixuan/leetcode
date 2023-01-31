"""
存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。

给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。

"""

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:


        # 方法一：状态压缩 + 广度优先搜索 + 哈希表
        # 时间复杂度：O(2^n * n^2)
        # 空间复杂度：O(n * 2^n)
        n = len(graph)
        queue = [(i, 1 << i, 0) for i in range(n)]
        seen = {(i, 1 << i) for i in range(n)} # 哈希表

        while queue:
            node, mask, depth = queue.pop(0)
            if mask == (1 << n) - 1:
                return depth
            for next_node in graph[node]:
                mask_next = mask | (1 << next_node)
                if (next_node, mask_next) not in seen:
                    queue.append((next_node, mask_next, depth + 1))
                    seen.add((next_node, mask_next))


        # 方法二：floyd算法 + 状态压缩 + 动态规划
        # 时间复杂度：O(2^n * n^2)
        # 空间复杂度：O(n * 2^n)
        n = len(graph)
        dist = [[float('inf')] * n for _ in range(n)] # 两点之间的距离
        for i in range(n):
            for j in graph[i]:
                dist[i][j] = 1

        # floyd算法计算两点间的距离
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        #print(dist)
        dp = [[float('inf')] * (1 << n) for _ in range(n)] # 动态规划

        for mask in range(1, 1 << n):
            if mask & (mask-1) == 0:  # 只有一个1
                u = bin(mask).count("0") - 1
                dp[u][mask] = 0
            else:
                for u in range(n):
                    if mask & (1 << u):
                        for v in range(n):
                            if mask & (1 << v) and u != v:
                                dp[u][mask] = min(dp[u][mask], dp[v][mask ^ (1 << u)] + dist[v][u])

        #print(dp)
        return min(dp[u][(1 << n) - 1] for u in range(n))







