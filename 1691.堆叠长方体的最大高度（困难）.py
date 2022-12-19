"""
给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi, heighti]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。
如果 widthi <= widthj 且 lengthi <= lengthj 且 heighti <= heightj ，你就可以将长方体 i 堆叠在长方体 j 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。

返回 堆叠长方体 cuboids 可以得到的 最大高度 。

示例 1：
输入：cuboids = [[50,45,20],[95,37,53],[45,23,12]]
输出：190
解释：
第 1 个长方体放在底部，53x37 的一面朝下，高度为 95 。
第 0 个长方体放在中间，45x20 的一面朝下，高度为 50 。
第 2 个长方体放在上面，23x12 的一面朝下，高度为 45 。
总高度是 95 + 50 + 45 = 190 。

示例 2：
输入：cuboids = [[38,25,45],[76,35,3]]
输出：76
解释：
无法将任何长方体放在另一个上面。
选择第 1 个长方体然后旋转它，使 35x3 的一面朝下，其高度为 76 。

示例 3：
输入：cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
输出：102
解释：
重新排列长方体后，可以看到所有长方体的尺寸都相同。
你可以把 11x7 的一面朝下，这样它们的高度就是 17 。
堆叠长方体的最大高度为 6 * 17 = 102 。
 
提示：
n == cuboids.length
1 <= n <= 100
1 <= widthi, lengthi, heighti <= 100

"""

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:


        # 方法一：贪心 + 记忆化搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(cuboids)
        for cuboid in cuboids:
            cuboid.sort(reverse=True)
        cuboids.sort(key=sum, reverse=True)
        #print(cuboids)
        count = 0
        ans = 0
        #tmp_height = 0

        @cache
        def dfs(height, i):
            #print('height, i:', height, i)
            nonlocal ans
            ans = max(ans, height)
            if i != -1:
                a1, b1, c1 = cuboids[i][0], cuboids[i][1], cuboids[i][2]
                tmp = sorted([a1, b1, c1], reverse=True)
                a1, b1, c1 = tmp[0], tmp[1], tmp[2]
            else:
                a1, b1, c1 = inf, inf, inf
            #print('a1, b1, c1:', a1, b1, c1)
            for j in range(i + 1, n):
                a2, b2, c2 = cuboids[j][0], cuboids[j][1], cuboids[j][2]
                tmp = sorted([a2, b2, c2], reverse=True)
                a2, b2, c2 = tmp[0], tmp[1], tmp[2]
                if a1 >= a2 and ((b2 <= b1 and c2 <= c1) or (b2 <= c1 and c2 <= c1)):
                    dfs(height + a2, j)

        dfs(0, -1)
        return ans


        # 方法二：贪心 + 动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(cuboids)
        dp = [0] * (n + 1)   # 以第i + 1个方块为底
        for cuboid in cuboids:
            cuboid.sort(reverse=True)
        cuboids.sort(key=sum, reverse=False)

        for i, (a1, b1, c1) in enumerate(cuboids):
            dp[i + 1] = a1
            for j in range(i):
                a2, b2, c2 = cuboids[j][0], cuboids[j][1], cuboids[j][2]
                if a1 >= a2 and b1 >= b2 and c1 >= c2:
                    dp[i + 1] = max(dp[i + 1], dp[j + 1] + a1)
        return max(dp)


        # 方法三：贪心 + 记忆化搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(cuboids)
        for cuboid in cuboids:
            cuboid.sort(reverse=True)
        cuboids.sort(key=sum, reverse=False)
        #print(cuboids)
        count = 0
        ans = 0

        @cache
        def dfs(i):
            #print('i:', i)
            a1, b1, c1 = cuboids[i][0], cuboids[i][1], cuboids[i][2]
            #print('a1, b1, c1:', a1, b1, c1)  
            res = a1     
            for j in range(i):
                a2, b2, c2 = cuboids[j][0], cuboids[j][1], cuboids[j][2]
                if a1 >= a2 and b2 <= b1 and c2 <= c1:
                    res = max(res, a1 + dfs(j))
            #print('res:', res)
            return res

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans


        # 方法四：贪心 + 记忆化搜索
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        def check(a: List[int], b: List[int]) -> bool:
            return a[0] <= b[0] and a[1] <= b[1] and a[2] <= b[2]

        n = len(cuboids)
        for c in cuboids:
            c.sort()
        cuboids.sort(key=sum)

        @cache
        def dfs(top: int, index: int) -> int:
            if index == n:
                return 0
            height = dfs(top, index + 1)
            if top == -1 or check(cuboids[top], cuboids[index]):
                height = max(height, cuboids[index][2] + dfs(index, index + 1))
            return height
        return dfs(-1, 0) 



        



