"""
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
“最近的”定义为两个整数差的绝对值最小。
 
示例 1:
输入: n = "123"
输出: "121"

示例 2:
输入: n = "1"
输出: "0"
解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
 
提示:
1 <= n.length <= 18
n 只由数字组成
n 不含前导 0
n 代表在 [1, 10^18 - 1] 范围内的整数

"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:


        # 方法一：贪心
        # 时间复杂度：O(logn)
        # 空间复杂度：O(logn)
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        prefix = n[: (m + 1) // 2]
        #print(candidates)
        #print(prefix)
        for i in range(-1, 2):
            if m % 2 == 1:
                candidates.append(int(str(int(prefix) + i) + str(int(prefix) + i)[: m // 2][::-1]))
            else:
                candidates.append(int(str(int(prefix) + i) + str(int(prefix) + i)[::-1]))
        #print(candidates)

        ans = float('-inf')
        num = int(n)
        for candidate in candidates:
            if candidate == num:
                continue
            if ans == float('-inf') or abs(num - candidate) < abs(num - ans) or (abs(num - candidate) == abs(num - ans) and candidate < ans):
                ans = candidate

        return str(ans)




        
