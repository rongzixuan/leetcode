"""
在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。

花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。

给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i 处的水龙头，可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。

请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。

示例 1：
输入：n = 5, ranges = [3,4,1,1,0,0]
输出：1
解释：
点 0 处的水龙头可以灌溉区间 [-3,3]
点 1 处的水龙头可以灌溉区间 [-3,5]
点 2 处的水龙头可以灌溉区间 [1,3]
点 3 处的水龙头可以灌溉区间 [2,4]
点 4 处的水龙头可以灌溉区间 [4,4]
点 5 处的水龙头可以灌溉区间 [5,5]
只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。

示例 2：
输入：n = 3, ranges = [0,0,0,0]
输出：-1
解释：即使打开所有水龙头，你也无法灌溉整个花园。
 
提示：
1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100

"""

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:


        # 方法一：贪心
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        #n = len(ranges)
        #print(n)
        edges = []
        for i, rg in enumerate(ranges):
            edges.append([i - rg, i + rg])
        #print(edges)
        edges.sort()
        #print(edges)

        ans = 0
        pre = 0
        i = 0
        while i <= n:
            #print(i)
            nxt = 0
            if edges[i][0] > pre:
                return -1
            if i >= n:
                return ans        
            while i <= n and edges[i][0] <= pre:
                nxt = max(nxt, edges[i][1])
                i += 1           
            pre = nxt
            ans += 1
            if nxt >= n:
                return ans
        return ans


        # 方法二：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        last = [0] * (n + 1)
        for i, x in enumerate(ranges):
            l, r = max(0, i - x), i + x
            last[l] = max(last[l], r)
        #print('last:', last)

        ans = mx = pre = 0
        for i in range(n):
            mx = max(mx, last[i])
            if mx <= i:
                return -1
            if pre == i:
                ans += 1
                pre = mx
        return ans




