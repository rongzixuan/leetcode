"""
有一个具有 n 个顶点的 双向 图，其中每个顶点标记从 0 到 n - 1（包含 0 和 n - 1）。图中的边用一个二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和顶点 vi 之间的双向边。 每个顶点对由 最多一条 边连接，并且没有顶点存在与自身相连的边。
请你确定是否存在从顶点 source 开始，到顶点 destination 结束的 有效路径 。

给你数组 edges 和整数 n、source 和 destination，如果从 source 到 destination 存在 有效路径 ，则返回 true，否则返回 false 。

示例 1：
输入：n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
输出：true
解释：存在由顶点 0 到顶点 2 的路径:
- 0 → 1 → 2 
- 0 → 2

示例 2：
输入：n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
输出：false
解释：不存在由顶点 0 到顶点 5 的路径.
 
提示：
1 <= n <= 2 * 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
不存在重复边
不存在指向顶点自身的边

"""

class Union:
    def __init__(self, n):
        self.height = [0] * n
        self.parent = list(range(n))

    def findParent(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def connect(self, x, y):
        x, y = self.findParent(x), self.findParent(y)
        if x == y:
            return
        elif self.height[x] > self.height[y]:
            self.parent[y] = x
        elif self.height[y] > self.height[x]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.height[x] += 1


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        # 方法一：广度优先搜索
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(m + n)
        # m = len(edges)
        conn = [[] for _ in range(n)]
        for x, y in edges:
            conn[x].append(y)
            conn[y].append(x)
        #print(conn)

        queue = [source]
        used = set()
        used.add(source)
        while queue:
            for _ in range(len(queue)):
                x = queue.pop(0)
                if x == destination:
                    return True
                for y in conn[x]:
                    if y not in used:
                        queue.append(y)
                        used.add(y)
        return False


        # 方法二：深度优先搜索
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(m + n)
        # m = len(edges)
        conn = [[] for _ in range(n)]
        for x, y in edges:
            conn[x].append(y)
            conn[y].append(x)
        #print(conn)

        queue = [source]
        used = set()
        used.add(source)
        while queue:
            for _ in range(len(queue)):
                x = queue.pop(-1)
                if x == destination:
                    return True
                for y in conn[x]:
                    if y not in used:
                        queue.append(y)
                        used.add(y)
        return False


        # 方法三：深度优先搜索
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(m + n)
        # m = len(edges)
        conn = [[] for _ in range(n)]
        for x, y in edges:
            conn[x].append(y)
            conn[y].append(x)

        used = set()
        used.add(source)
        def dfs(x):
            #print(x)
            if x == destination:
                return True
            flag = False
            for y in conn[x]:
                if y not in used:
                    used.add(y)
                    if dfs(y):
                        flag = True
                        break
                    #used.remove(y)
            return flag
        
        return True if dfs(source) else False


        # 方法四：并查集
        # 时间复杂度：O(m + n)
        # 空间复杂度：O(m + n)
        # m = len(edges)
        union = Union(n)
        for x, y in edges:
            union.connect(x, y)

        return union.findParent(source) == union.findParent(destination)








