"""
超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内

"""

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:


        # 方法一：最小堆
        # 时间复杂度：O(nmlognm)
        # 空间复杂度：O(mn)
        # 其中，m为primes数组长度
        seen = {1}
        heap = [1]

        for i in range(n):
            ugly = heapq.heappop(heap)
            for prime in primes:
                num = prime * ugly
                if num not in seen:
                    seen.add(num)
                    heapq.heappush(heap, num)

        return ugly


        # 方法二：动态规划
        # 时间复杂度：O(nm)
        # 空间复杂度：O(n+m)
        # 其中，m为primes数组长度
        dp = [0] * (n+1)
        dp[1] = 1
        m = len(primes)

        point = defaultdict(List)
        for i in range(m):
            point[i] = 1

        for i in range(2, n+1):
            min_num = min(dp[point[j]] * primes[j] for j in range(m))
            dp[i] = min_num
            for j in range(m):
                if dp[point[j]] * primes[j] == min_num:
                    point[j] += 1

        #print(dp)
        return dp[n]


