"""
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 ， 其中 n > 2 。

数据保证对于给定的 k ，一定能找到可行解。

示例 1：
输入：k = 7
输出：2 
解释：斐波那契数字为：1，1，2，3，5，8，13，……
对于 k = 7 ，我们可以得到 2 + 5 = 7 。

示例 2：
输入：k = 10
输出：2 
解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。

示例 3：
输入：k = 19
输出：3 
解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。

提示：
1 <= k <= 10^9

"""


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:


        # 方法一：贪心（超时）
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if k == 1 or k == 2:
            return 1

        #dp = [1, 1]
        a, b, c = 1, 1, 2
        count = {1, 1}
        while c <= k:
            #dp.append(c)
            count.add(c)
            #print('c:', c)
            a, b, c = b, c, b + c

        res = 1
        k -= b
        tmp_k = k
        while k:  
            #print('k:', k)          
            if tmp_k in count:
                k -= tmp_k
                res += 1
                tmp_k = k
            else:
                while tmp_k not in count:
                    #print('tmp_k:', tmp_k)
                    tmp_k -= 1

        return res


        # 方法二：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if k == 1 or k == 2:
            return 1

        dp = [1, 1]
        a, b, c = 1, 1, 2
        count = {1, 1}
        while c <= k:
            dp.append(c)
            #count.add(c)
            #print('c:', c)
            a, b, c = b, c, b + c

        res = 0
        #k -= b
        #tmp_k = k
        i = len(dp) - 1
        while k:  
            #print('k:', k)          
            while dp[i] > k:
                i -= 1
            k -= dp[i]
            res += 1

        return res





