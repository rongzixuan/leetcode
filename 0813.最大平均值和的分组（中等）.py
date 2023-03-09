"""
给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。

注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。

返回我们所能得到的最大 分数 是多少。答案误差在 10-6 内被视为是正确的。

示例 1:
输入: nums = [9,1,2,3,9], k = 3
输出: 20.00000
解释: 
nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20. 
我们也可以把 nums 分成[9, 1], [2], [3, 9]. 
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.

示例 2:
输入: nums = [1,2,3,4,5,6,7], k = 4
输出: 20.50000
 
提示:
1 <= nums.length <= 100
1 <= nums[i] <= 10^4
1 <= k <= nums.length

"""

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:


        # 方法一：前缀和 + 记忆化搜索
        # 时间复杂度：
        # 空间复杂度：
        """
        我们可以先预处理得到前缀和数组 s，方便快速得到子数组的和。

然后设计一个函数 dfs(i,k)，表示从数组下标 i 开始，最多分成 k 组的最大平均值和。答案即为 dfs(0,k)。

函数 dfs(i,k) 的执行逻辑如下：

当 i=n 时，表示已经遍历到数组末尾，此时返回 0。
当 k=1 时，表示只剩下一组，此时返回从下标 i 开始到数组末尾的平均值。
否则，我们在 [i,..n−1] 的范围内枚举分组的结束位置 j，计算从下标 i 到下标 j 的平均值，以及从下标 j+1 开始，最多分成 k−1 组的最大平均值和。取其中的最大值作为答案。
为了避免重复计算，我们可以用数组 f 记忆化函数 dfs(i,k) 的返回值。
        """
        @cache
        def dfs(i, k):
            if i == n:
                return 0
            if k == 1:
                return (s[-1] - s[i]) / (n - i)
            ans = 0
            for j in range(i, n):
                t = (s[j + 1] - s[i]) / (j - i + 1) + dfs(j + 1, k - 1)
                ans = max(ans, t)
            return ans

        n = len(nums)
        s = list(accumulate(nums, initial=0))
        return dfs(0, k)


        # 方法二：前缀和 + 动态规划
        # 时间复杂度：
        # 空间复杂度：
        n = len(nums)
        prefix = list(accumulate(nums, initial=0))
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i
        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for x in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefix[i] - prefix[x]) / (i - x))
        return dp[n][k]






