"""
树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。

给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。

请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。

示例 1：
输入：n = 4, edges = [[1,0],[1,2],[1,3]]
输出：[1]
解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。

示例 2：
输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
输出：[3,4]

提示：
1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
所有 (ai, bi) 互不相同
给定的输入 保证 是一棵树，并且 不会有重复的边

"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:


        # 方法一：广度优先搜索（超时）
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        connect = [[] for _ in range(n)]
        for x, y in edges:
            connect[x].append(y)
            connect[y].append(x)


        min_depth = 10 ** 5
        ans = []
        for i in range(n):
            stack = deque([(i, 1)])
            used = {i}
            tmp_depth = 1
            while stack:
                node, depth = stack.popleft()
                for new_node in connect[node]:
                    if new_node not in used:
                        stack.append((new_node, depth + 1))
                        used.add(new_node)
                        tmp_depth = depth + 1
            if tmp_depth == min_depth:
                ans.append(i)
            elif tmp_depth < min_depth:
                min_depth = tmp_depth
                ans = [i]

        return ans


        # 方法二：广度优先搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if n == 1:
            return [0]

        connect = [[] for _ in range(n)]
        degree = [0] * n
        for x, y in edges:
            connect[x].append(y)
            connect[y].append(x)
            degree[x] += 1
            degree[y] += 1

        queue = deque()
        for x, d in enumerate(degree):
            if d == 1:
                queue.append(x)

        ans = []
        while queue:
            length = len(queue)
            ans = []
            for i in range(length):
                node = queue.popleft()
                ans.append(node)
                for new_node in connect[node]:
                    degree[new_node] -= 1
                    if degree[new_node] == 1:
                        queue.append(new_node)


        return ans


        # 方法三：拓扑排序
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if n == 1:
            return [0]

        connect = [[] for _ in range(n)]
        degree = [0] * n
        for x, y in edges:
            connect[x].append(y)
            connect[y].append(x)
            degree[x] += 1
            degree[y] += 1

        queue = [i for i, d in enumerate(degree) if d == 1]
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(queue)
            tmp_queue = queue
            queue = []
            for node in tmp_queue:
                for new_node in connect[node]:
                    degree[new_node] -= 1
                    if degree[new_node] == 1:
                        queue.append(new_node)

        return queue


