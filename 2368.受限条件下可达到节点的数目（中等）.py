"""
现有一棵由 n 个节点组成的无向树，节点编号从 0 到 n - 1 ，共有 n - 1 条边。
给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。另给你一个整数数组 restricted 表示 受限 节点。

在不访问受限节点的前提下，返回你可以从节点 0 到达的 最多 节点数目。

注意，节点 0 不 会标记为受限节点。

示例 1：
输入：n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
输出：4
解释：上图所示正是这棵树。
在不访问受限节点的前提下，只有节点 [0,1,2,3] 可以从节点 0 到达。

示例 2：
输入：n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
输出：3
解释：上图所示正是这棵树。
在不访问受限节点的前提下，只有节点 [0,5,6] 可以从节点 0 到达。

提示：
2 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges 表示一棵有效的树
1 <= restricted.length < n
1 <= restricted[i] < n
restricted 中的所有值 互不相同

"""

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        
        # 方法一：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        """roads = [[-1] * n for _ in range(n)]
        #print(roads)
        for x, y in edges:
            roads[x][y] = 1
            roads[y][x] = 1"""
        roads = [[] for _ in range(n)]
        #print(roads)
        for x, y in edges:
            roads[x].append(y)
            roads[y].append(x)    
        #print(roads)
        restricted_set = set(restricted)
            
        queue = deque([0])
        ans = set([0])
        while queue:
            x = queue.popleft()
            for i, y in enumerate(roads[x]):
                if y not in ans and y not in restricted_set:
                    queue.append(y)
                    ans.add(y)
                    
        return len(ans)
        
        
        
        
        
