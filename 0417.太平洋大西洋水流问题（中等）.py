"""
有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。

这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。

岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋 。


示例 1：

输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]\

示例 2：
输入: heights = [[2,1],[1,2]]
输出: [[0,0],[0,1],[1,0],[1,1]]

提示：
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5

"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        # 方法一：深度优先搜索
        # 时间复杂度：O(m^2 * n^2)
        # 空间复杂度：O(m * n)
        m, n = len(heights), len(heights[0])

        def dfs(i, j):
            #print(i, j)
            visited[i][j] = True
            flag1, flag2 = False, False
            if (i == 0 or j == 0) and heights[i][j] >= 0:
                flag1 = True
            if (i == m - 1 or j == n - 1) and heights[i][j] >= 0:
                flag2 = True
            
            if flag1 and flag2:
                new_set = []
            #lif flag1:
            #    new_set = [(i+1, j), (i, j+1)]
            #elif flag2:
            #    new_set = [(i-1, j), (i, j-1)]
            else:
                new_set = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            
            for new_i, new_j in new_set:
                if 0 <= new_i < m and 0 <= new_j < n and heights[new_i][new_j] <= heights[i][j] and visited[new_i][new_j] == False:
                    if (new_i, new_j) in ans:
                        flag1, flag2 = True, True
                        break
                    flag1_new, flag2_new = dfs(new_i, new_j)
                    if flag1_new:
                        flag1 = True
                    if flag2_new:
                        flag2 = True
                    if flag1 and flag2:
                        break

            visited[i][j] = False
            return flag1, flag2
      
        ans = set()
        visited = [[False] * n for _ in range(m)]
        #print('visited:', visited)
        for i, j in product(range(m), range(n)):
            #print('i, j:', i, j)
            #print('visited:', visited)
            pacific_flag, atlantic_flag = dfs(i, j)
            if pacific_flag and atlantic_flag:
                ans.add((i, j))
        return list(ans)


        # 方法二：深度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        m, n = len(heights), len(heights[0])

        def search(starts):
            ans = set()
            def dfs(i, j): 
                if (i, j) in ans:
                    return               
                ans.add((i, j))
                for new_i, new_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= new_i < m and 0 <= new_j < n and heights[new_i][new_j] >= heights[i][j]:
                        dfs(new_i, new_j)

            for i, j in starts:
                dfs(i, j)
            return ans

        starts1 = [(i, 0) for i in range(m)] \
                + [(0, j) for j in range(1, n)] 

        starts2 = [(i, n - 1) for i in range(m - 1)] \
                + [(m - 1, j) for j in range(n)]
        #print('starts1:', starts1)
        #print('starts2:', starts2)
        #print(search(starts1))
        #print(search(starts2))
        return list(search(starts1) & search(starts2))


        # 方法三：广度优先搜索
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        from collections import deque
        m, n = len(heights), len(heights[0])
        
        def bfs(starts):
            queue = deque(starts)
            ans = set(starts)
            while queue:
                i, j = queue.popleft()
                for new_i, new_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= new_i < m and 0 <= new_j < n and heights[new_i][new_j] >= heights[i][j] and (new_i, new_j) not in ans:
                        queue.append((new_i, new_j))
                        ans.add((new_i, new_j))
            return ans

        starts1 = [(i, 0) for i in range(m)] \
                + [(0, j) for j in range(1, n)] 
        starts2 = [(i, n - 1) for i in range(m - 1)] \
                + [(m - 1, j) for j in range(n)]
        return list(bfs(starts1) & bfs(starts2))   








        





