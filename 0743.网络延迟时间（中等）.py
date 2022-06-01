"""
有 n 个网络节点，标记为 1 到 n。
给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # 方法一：dijkstra算法
        # 时间复杂度：O(m + n^2)
        # 空间复杂度：O(n^2)
        # m为边的个数
        dists = [[float('inf')] * n for _ in range(n)]
        for i, j, time in times:
            dists[i-1][j-1] = time
        #print('dists:', dists)
        #print(dists[k-1])
        
        min_dists = [float('inf')] * n
        min_dists[k-1] = 0
        used = [False] * n
       
        for _ in range(n):
            min_i = -1
            for i, used_flag in enumerate(used):
                if not used_flag and (min_i == -1 or min_dists[i] < min_dists[min_i]):
                    min_i = i
            used[min_i] = True

            #print('min_dists:', min_dists)
            for j in range(n):
                min_dists[j] = min(min_dists[j], min_dists[min_i] + dists[min_i][j])
        #print('min_dists:', min_dists)

        max_dist = max(min_dists)
        return max_dist if max_dist != float('inf') else -1


        # 方法二：dijkstra算法 + 小根堆
        # 时间复杂度：O(mlogm)
        # 空间复杂度：O(n+m)
        # m为边的个数
        dists = [[] * n for _ in range(n)]

        for i, j, time in times:
            #dists[i-1][j-1] = time
            dists[i-1].append((j-1, time))
        #print(dists)

        heap = [(0, k-1)]
        min_dists = [float('inf')] * n
        min_dists[k-1] = 0

        while heap:
            time, i = heapq.heappop(heap)
            if time > min_dists[i]:
                continue
            for j, time in dists[i]:
                new_time = min_dists[i] + time
                if new_time < min_dists[j]:
                    min_dists[j] = new_time
                    heapq.heappush(heap, (new_time, j))

        #print(min_dists)

        max_dist = max(min_dists)
        return max_dist if max_dist != float('inf') else -1

