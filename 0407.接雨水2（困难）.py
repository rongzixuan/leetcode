"""
给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

示例 1:
输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
输出: 4
解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。

示例 2:
输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
输出: 10

"""

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:


        # 方法一：广度优先搜索
        # 时间复杂度：O(m^2 * n^2)
        # 空间复杂度：O(m * n)
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 and n < 3:
            return 0

        queue = []
        max_height = max(max(row) for row in heightMap) # 最高柱     
        volumns = [[max_height] * n for _ in range(m)] 
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1) or (j == 0 or j == n-1):
                    volumns[i][j] = heightMap[i][j]
                    queue.append((i, j))
      
        res = 0
        while queue:
            i, j = queue.pop(0)
            #print(i, j)
            #res += volumns[i][j] - heightMap[i][j]
            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 < new_i < m-1 and 0 < new_j < n-1:
                    if volumns[i][j] < volumns[new_i][new_j] and volumns[new_i][new_j] > heightMap[new_i][new_j]:  
                        volumns[new_i][new_j] = max(volumns[i][j], heightMap[new_i][new_j])
                        queue.append((new_i, new_j))

        for i in range(m):
            for j in range(n):
                res += volumns[i][j] - heightMap[i][j]

        return res


        # 方法二：最小堆 + 广度优先搜索（栈）
        # 时间复杂度：O(m * n * log(m+n))
        # 空间复杂度：O(m * n)
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 and n < 3:
            return 0

        import heapq
        hq = [] # 最小堆
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    visited[i][j] = 1
                    heapq.heappush(hq, (heightMap[i][j], (i, j)))
                    #heapq.heappush(hq, (heightMap[i][j], i * n + j))
        #print('hq before:', hq)
        #print(visited)

        res = 0
        while hq:
            cur_height, (i, j) = heapq.heappop(hq)
            #cur_height, k = heapq.heappop(hq)
            #i, j = k // n, k % n
            #print(cur_height, i, j)
            for new_i, new_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 < new_i < m-1 and 0 < new_j < n-1 and visited[new_i][new_j] == 0:
                    if cur_height > heightMap[new_i][new_j]:
                        res += cur_height - heightMap[new_i][new_j]                   
                        #heapq.heappush(hq, (cur_height, new_i * n + new_j))
                        heapq.heappush(hq, (cur_height, (new_i, new_j)))
                    else:
                        #heapq.heappush(hq, (heightMap[new_i][new_j], new_i * n + new_j))
                        heapq.heappush(hq, (heightMap[new_i][new_j], (new_i, new_j)))
                    visited[new_i][new_j] = 1
            #print('hq:', hq)

        return res

    
    
    
