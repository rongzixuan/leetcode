"""
给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。

示例 1：
输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。

示例 2：
输入：n = 3
输出：["1/2","1/3","2/3"]

示例 3：
输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。

示例 4：
输入：n = 1
输出：[]

提示：
1 <= n <= 100

"""


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:


        # 方法一：数学
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        # 辗转相减法
        def check(i, j):
            while i != j:
                if i > j:
                    i -= j
                else:
                    j -= i
            return True if i == 1 else False

        ans = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if check(i, j):
                    ans .append(str(j) + '/' + str(i))

        return ans


        # 方法二：数学2
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        # 辗转相除法
        def check(i, j):
            m, n = max(i, j), min(i, j)
            r = m % n
            while r:
                m = n
                n = r
                r = m % n
            return True if n == 1 else False

        ans = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if check(i, j):
                    ans .append(str(j) + '/' + str(i))

        return ans

    
    
    
