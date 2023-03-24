"""
假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。

然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。

给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回 所有可能的无矛盾球队中得分最高那支的分数 。

示例 1：
输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
输出：34
解释：你可以选中所有球员。

示例 2：
输入：scores = [4,5,6,5], ages = [2,1,2,1]
输出：16
解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。

示例 3：
输入：scores = [1,2,3,5], ages = [8,9,10,1]
输出：6
解释：最佳的选择是前 3 名球员。
 
提示：
1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 10^6
1 <= ages[i] <= 1000

"""

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x, val):
        while x <= self.n:
            self.c[x] = max(self.c[x], val)
            x += x & -x           

    def query(self, x):
        s = 0
        while x:
            s = max(s, self.c[x])
            #x -= x & -x
            x &= (x - 1)
        return s


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:


        # 方法一：排序 + 动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(scores)
        arr = sorted(zip(scores, ages))
        #print(arr)

        dp = [0] * n
        for i in range(n):
            dp[i] = arr[i][0]
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    dp[i] = max(dp[i], arr[i][0] + dp[j])
        return max(dp)


        # 方法二：排序 + 动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(scores)
        arr = sorted(zip(ages, scores))

        dp = [0] * n
        for i in range(n):
            dp[i] = arr[i][1]
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    dp[i] = max(dp[i], arr[i][1] + dp[j])
        return max(dp)


        # 方法三：排序 + 基于值域
        # 时间复杂度：O(nlogn + nC)
        # 空间复杂度：O(n)
        # C = max(ages)
        #maxSum[x] 表示年龄最大值恰好等于 x 的球队最大分数和
        max_sum = [0] * (max(ages) + 1)
        for score, age in sorted(zip(scores, ages)):
            max_sum[age] = max(max_sum[:age + 1]) + score
        #print(max_sum)
        return max(max_sum)


        # 方法四：树状数组
        # 时间复杂度：O()
        # 空间复杂度：O(n)
        m = max(ages)
        tree = BinaryIndexedTree(m)
        for score, age in sorted(zip(scores, ages)):
            tree.update(age, score + tree.query(age))
        return tree.query(m)



