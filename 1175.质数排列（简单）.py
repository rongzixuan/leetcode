"""
请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。

示例 1：
输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。

示例 2：
输入：n = 100
输出：682289015
 
提示：
1 <= n <= 100

"""

class Solution:
    def numPrimeArrangements(self, n: int) -> int:


        # 方法一：数学
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        def isPrime(num):
            if num == 1 or num == 3:
                return True
            if num == 2:
                return False
            i = 2
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 1
            return True

        count1, count2 = 0, 0
        for i in range(1, n + 1):
            if isPrime(i):
                #print('true:', i)
                count1 += 1
            else:
                #print('false:', i)
                count2 += 1
        #print(count1, count2)

        ans = 1
        for i in range(1, count1 + 1):
            ans *= i 
        for i in range(1,count2 + 1):
            ans *= i
        return ans % (10 ** 9 + 7)


