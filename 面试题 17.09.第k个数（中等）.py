"""
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:
输入: k = 5
输出: 9

"""

class Solution:
    def getKthMagicNumber(self, k: int) -> int:


        # 方法一：优先队列(最小堆)
        # 时间复杂度：O(klogk)
        # 空间复杂度：O(k)
        heap = [1]
        used = set([1])
        import heapq as hp
        i, j = 0, 1
        while i < k - 1:
            if heap[0] * 3 not in used:
                hp.heappush(heap, heap[0] * 3)
                used.add(heap[0] * 3)
                j += 1
            if heap[0] * 5 not in used:
                hp.heappush(heap, heap[0] * 5)
                used.add(heap[0] * 5)
                j += 1
            if heap[0] * 7 not in used:
                hp.heappush(heap, heap[0] * 7)
                used.add(heap[0] * 7)
                j += 1
            i += 1
            hp.heappop(heap)
            #print(heap)

        #print('heap:', heap)
        return heap[0]


        # 方法二：动态规划
        # 时间复杂度：O(k)
        # 空间复杂度：O(k)
        dp = [0] * (k + 1)
        dp[1] = 1
        p3 = p5 = p7 = 1

        for i in range(2, k + 1):
            num3, num5, num7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(num3, num5, num7)
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
            if dp[i] == num7:
                p7 += 1
        
        return dp[k]





