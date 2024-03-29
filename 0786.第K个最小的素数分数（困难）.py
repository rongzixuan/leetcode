"""
给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数  组成，且其中所有整数互不相同。
对于每对满足 0 < i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。

示例 1：
输入：arr = [1,2,3,5], k = 3
输出：[2,5]
解释：已构造好的分数,排序后如下所示: 
1/5, 1/3, 2/5, 1/2, 3/5, 2/3
很明显第三个最小的分数是 2/5

示例 2：
输入：arr = [1,7], k = 1
输出：[1,7]
 
提示：
2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 10^4
arr[0] == 1
arr[i] 是一个 素数 ，i > 0
arr 中的所有数字 互不相同 ，且按 严格递增 排序
1 <= k <= arr.length * (arr.length - 1) / 2

"""

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:


        # 方法一：暴力法
        # 时间复杂度：O(n ^ 2)
        # 空间复杂度：O(n ^ 2)
        n = len(arr)
        res = []

        for i in range(n):
            for j in range(i+1, n):
                res.append((arr[i] / arr[j], [arr[i], arr[j]]))

        res.sort(key=lambda x: x[0])
        #print(res)
        return res[k-1][1]


        # 方法二：优先队列
        # 时间复杂度：
        # 空间复杂度：
        n = len(arr)

        heap = []
        for i in range(n):
            heapq.heappush(heap, (1 / arr[i], 0, i))

        for k in range(k):
            val, i, j = heapq.heappop(heap)
            #print(val, i, j)
            if i + 1 < j:
                heapq.heappush(heap, (arr[i+1] / arr[j], i+1, j))

        return [arr[i], arr[j]]


        # 方法三：二分查找 + 双指针
        # 时间复杂度：
        # 空间复杂度：
        n = len(arr)
        res = []

        left, right = 0.0, 1.0  # 分数
        while True:
            #print(left, right)
            mid = left + (right - left) / 2
            print('mid:', mid)

            i = -1
            count = 0
            x, y = 0, 1
            for j in range(1, n):
                #print('i, j:', i, j)
                while arr[i+1] / arr[j] < mid:
                    i += 1
                    if arr[i] / arr[j] > x / y:
                        x, y = arr[i], arr[j]
                count += (i+1)
            #print(count)

            if count == k:
                return [x, y]
            elif count > k:
                right = mid
            else:
                left = mid












