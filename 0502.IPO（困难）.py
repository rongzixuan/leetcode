"""
假设 力扣（LeetCode）即将开始 IPO 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。
给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。

最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。

答案保证在 32 位有符号整数范围内.

"""


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:


        # 方法一：优先队列（最大堆） + 贪心（超时）
        # 时间复杂度：O(k*(n+logn))
        # 空间复杂度：O(n)
        n = len(profits)
        import heapq
        heap = []
        count = 0
        res = 0

        for i in range(n):
            if capital[i] <= w:
                heap.append((-profits[i], i))
        #print(heap)
        heapq.heapify(heap)
        #print(heap)

        if heap == []:
            return 0

        while count < k and heap:
            tmp_profit, tmp_i = heapq.heappop(heap)
            #print('tmp_profit, tmp_i:', tmp_profit, tmp_i)
            new_w = w - tmp_profit
            #print(res)
            count += 1
            for i in range(n):
                if w < capital[i] <= new_w:
                    heap.append((-profits[i], i))
            w = new_w
            #print(heap)
            heapq.heapify(heap)
            #print(heap)

        return w


        # 方法二：优先队列（最大堆） + 贪心
        # 时间复杂度：O(nlogn + klogn)
        # 空间复杂度：O(n)
        n = len(profits)
        import heapq
        heap = []
        count = 0
        arr = []
        cur = 0

        for i in range(n):
            arr.append([capital[i], profits[i]])
        arr.sort(key = lambda x: x[0])
        #print(arr)

        while count < k:
            while cur < n and arr[cur][0] <= w:
                heapq.heappush(heap, -arr[cur][1])
                cur += 1
            #print(heap)

            if heap:
                w -= heapq.heappop(heap)
                count += 1
            else:
                break

        return w


    
