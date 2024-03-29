"""
在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。

对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。

返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。

该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，满足 (i, j) 是图的一条有向边

"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        #print(graph)


        # 方法一：dfs + 三色标记法
        # 时间复杂度：O(m+n)，其中m为边的个数，n为节点的个数
        # 空间复杂度：O(n)
        n = len(graph)
        colors = [0] * n   # 0：未访问，1：正在访问或不安全，2：无环，安全

        def safe(x):
            if colors[x] > 0:
                return colors[x] == 2
            colors[x] = 1
            for y in graph[x]: # 的方式搜索是否在环中
                if not safe(y):
                    return False
            colors[x] = 2
            return True

        return [x for x in range(n) if safe(x)]



        # 方法二：拓扑排序法
        # 时间复杂度：O(m+n)
        # 空间复杂度：O(m+n)

        rg = [[] for _ in graph]
        #print(rg)

        for x, ys in enumerate(graph):
            for y in ys:
                rg[y].append(x)
        #print(rg)
        in_deg = [len(ys) for ys in graph]
        #print(in_deg)

        q = deque([i for i, d in enumerate(in_deg) if d == 0])
        #print(q)

        while q:
            for x in rg[q.popleft()]:
                in_deg[x] -= 1
                if in_deg[x] == 0:
                    q.append(x)
        #print(in_deg)            

        return [i for i, d in enumerate(in_deg) if d == 0]



