"""
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

例 1：
输入: m = 3, n = 3, k = 5
输出: 3

解释: 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).

例 2：
输入: m = 2, n = 3, k = 6
输出: 6

解释: 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).

注意：
m 和 n 的范围在 [1, 30000] 之间。
k 的范围在 [1, m * n] 之间。

"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:


        # 方法一：优先队列（超时）
        # 时间复杂度：O(m * n * klogk)
        # 空间复杂度：O(k)
        import heapq
        queue = []

        for i, j in product(range(1, m+1), range(1, n+1)):
            if len(queue) < k:
                heapq.heappush(queue, -i * j)
            elif len(queue) == k and -queue[0] > i * j:
                heapq.heappop(queue)
                heapq.heappush(queue, -i * j)

        #print(len(queue))
        #print(queue)
        return -heapq.heappop(queue)


        # 方法二：二分法
        # 时间复杂度：O(m * n * logmn)
        # 空间复杂度：O(1)
        def getLowerNum(num):
            count = 0
            i = m
            for j in range(1, n + 1):
                while i > 0 and i * j > num:
                    i -= 1
                count += i
            return count

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            count = getLowerNum(mid)
            if count > k:
                right = mid
            elif count < k:
                left = mid + 1
            else:
                #print('mid:', mid)
                #return mid
                right = mid
        #print('left, right:', left, right)
        return right



