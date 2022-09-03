"""
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。

给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

示例：
输入：[[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4]
 
提示：
给出数对的个数在 [1, 1000] 范围内。

"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        pairs.sort()
        n = len(pairs)
        dp = [1] * n

        for i in range(1, n):
            for j in range(0, n):
                if i != j and pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


        # 方法二：贪心
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        n = len(pairs)
        pairs = sorted(pairs, key = lambda x: x[1])
        #print(pairs)

        cur = float('-inf')
        ans = 0
        for i in range(n):
            if pairs[i][0] > cur:
                ans += 1
                cur = pairs[i][1]
        return ans


        # 方法三：贪心 + 二分法
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        from bisect import bisect_left
        n = len(pairs)
        pairs = sorted(pairs, key = lambda x: x[1])

        arr = []
        for x, y in pairs:
            #print(x, y)
            if len(arr) == 0 or x > arr[-1]:
                arr.append(y)
            else:
                index = bisect_left(arr, y)
                #print(index)
                if index < len(arr):
                    arr[index] = y
        return len(arr)




