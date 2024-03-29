"""
给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。

子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。

示例 1：
输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。

示例 2：
输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。

示例 3：
输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。
 
提示：
1 <= arr.length <= 10^5
-10^4 <= arr[i], difference <= 10^4

"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:


        # 方法一：动态规划 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(arr)
        if n == 1:
            return 1

        from collections import defaultdict
        hash_table = defaultdict(list)
        dp = [1] * n
        for i in range(n):
            if arr[i] - difference in hash_table:
                dp[i] = dp[hash_table[arr[i] - difference][-1]]+ 1
            hash_table[arr[i]].append(i)
        #print(hash_table)

        return max(dp)


        # 方法二：动态规划 + 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(arr)
        if n == 1:
            return 1

        dp = defaultdict(int)
        for a in arr:
            dp[a] = dp[a-difference] + 1

        return max(dp.values())


    
    
    
