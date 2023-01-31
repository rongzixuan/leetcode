"""
给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为 [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。

例如，数组为 nums = [2,4,1,3,0]，我们按 k = 2 进行轮调后，它将变成 [1,3,0,2,4]。这将记为 3 分，因为 1 > 0 [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。

在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。

示例 1：
输入：nums = [2,3,1,4,0]
输出：3
解释：
下面列出了每个 k 的得分：
k = 0,  nums = [2,3,1,4,0],    score 2
k = 1,  nums = [3,1,4,0,2],    score 3
k = 2,  nums = [1,4,0,2,3],    score 3
k = 3,  nums = [4,0,2,3,1],    score 4
k = 4,  nums = [0,2,3,1,4],    score 3
所以我们应当选择 k = 3，得分最高。

示例 2：
输入：nums = [1,3,0,2,4]
输出：0
解释：
nums 无论怎么变化总是有 3 分。
所以我们将选择最小的 k，即 0。
 
提示：
1 <= nums.length <= 10^5
0 <= nums[i] < nums.length

"""


class Solution:
    def bestRotation(self, nums: List[int]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        """
        预处理+动态规划

        发现每次移动的时候，值对应下标-1，首位到末位； 本来比下标小的依旧得分，本来等于下标的失分，本来大于下标的依旧不得分，本来在下标0的移到n-1处得分； 状态转移为f[k] = f[k-1] + (k-1步时值与下标相等的元素个数) + 1; 要得到每个步数时值与下标相等的元素个数，可由每个元素移到与值相等的下标的步数O(N)得到
        """
        n = len(nums)
        dp = [0] * n
        count = 0
        for i in range(n):
            if nums[i] <= i:
                dp[i - nums[i]] += 1
                count += 1
            else:
                dp[i + n - nums[i]] += 1
        #print(dp)
        #print('count:', count)

        ans = 0
        max_count = count
        for i in range(1, n):
            count -= (dp[i - 1] - 1)
            #print('count:', count)
            if count > max_count:
                ans, max_count = i, count

        return ans




