"""
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
n >= 3
对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}

给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
（回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）

示例 1：
输入: arr = [1,2,3,4,5,6,7,8]
输出: 5
解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。

示例 2：
输入: arr = [1,3,7,11,12,14,18]
输出: 3
解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。

提示：
3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 10^9

"""

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(arr)
        dp = [[0] * n for _ in range(n)]   # dp[i][j]表示以第i个、第价格数字结尾的子序列包含的斐波那契数列最长的长度
        used = defaultdict(int)
        used[arr[0]] = 0
        used[arr[1]] = 1

        for i in range(2, n):           
            a = arr[i]
            #print('i, a:', i, a)
            for k, v in used.items():
                if a - k in used and k != a - k:
                    min_k, max_k = min(k, a - k), max(k, a - k)
                    #print('k, a - k:', k, a - k)
                    dp[used[max_k]][i] = max(dp[used[max_k]][i], dp[used[min_k]][used[max_k]] + 1, 3)
            used[a] = i

        #print('dp:', dp)
        #print('used:', used)
        return max(dp[i][j] for i in range(n) for j in range(n))



