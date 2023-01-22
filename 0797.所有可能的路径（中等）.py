"""
给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。

译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a 

"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:


        # 方法一：深度优先搜索
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(n)， 栈的开销
        res = [0]
        ans = []
        #print(graph)
        n = len(graph)

        def dfs(node, res):
            if node == n-1:
                ans.append(res[::1])
                return
            for next_node in graph[node]:
                res.append(next_node)
                dfs(next_node, res)
                res.pop(-1)

        dfs(0, res)
        return ans

    
    
    
    
