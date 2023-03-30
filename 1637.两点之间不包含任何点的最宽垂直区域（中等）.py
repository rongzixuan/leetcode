"""
给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直区域 的宽度。

垂直区域 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直区域 为宽度最大的一个垂直区域。

请注意，垂直区域 边上 的点 不在 区域内。

示例 1：
输入：points = [[8,7],[9,9],[7,4],[9,7]]
输出：1
解释：红色区域和蓝色区域都是最优区域。

示例 2：
输入：points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
输出：3
 
提示：
n == points.length
2 <= n <= 10^5
points[i].length == 2
0 <= xi, yi <= 10^9

"""

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:


        # 方法一：哈希表 + 排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        from collections import Counter, OrderedDict
        count = Counter([x for x, y in points])
        count_list = sorted(count.keys())
        #count = OrderedDict(count_list)
        #print(count_list)

        ans = 0
        for i in range(1, len(count_list)):
            num = count_list[i]
            #print(i, num)
            if num - count_list[i - 1] > ans:
                ans = num - count_list[i - 1]
        return ans


        # 方法二：排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        points.sort()
        return max(b[0] - a[0] for a, b in pairwise(points))


        # 方法三：桶排序
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        nums = [x for x, _ in points]
        n = len(nums)
        mi, mx = min(nums), max(nums)
        bucket_size = max(1, (mx - mi) // (n - 1))
        bucket_count = (mx - mi) // bucket_size + 1
        buckets = [[inf, -inf] for _ in range(bucket_count)]
        for x in nums:
            i = (x - mi) // bucket_size
            buckets[i][0] = min(buckets[i][0], x)
            buckets[i][1] = max(buckets[i][1], x)
        #print('buckets:', buckets)

        ans = 0
        prev = inf
        for curmin, curmax in buckets:
            if curmin > curmax:
                continue
            ans = max(ans, curmin - prev)
            prev = curmax
        return ans







