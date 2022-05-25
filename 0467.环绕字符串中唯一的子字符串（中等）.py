"""
把字符串 s 看作是 “abcdefghijklmnopqrstuvwxyz” 的无限环绕字符串，所以 s 看起来是这样的：

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." . 
现在给定另一个字符串 p 。返回 s 中 唯一 的 p 的 非空子串 的数量 。 

示例 1:
输入: p = "a"
输出: 1
解释: 字符串 s 中只有一个"a"子字符。

示例 2:
输入: p = "cac"
输出: 2
解释: 字符串 s 中的字符串“cac”只有两个子串“a”、“c”。.

示例 3:
输入: p = "zab"
输出: 6
解释: 在字符串 s 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。
 
提示:
1 <= p.length <= 10^5
p 由小写英文字母构成

"""


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:


        # 方法一：动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(C)
        # C = 26
        dp = defaultdict(int)
        n = len(p)
        k = 0

        for i in range(n):
            if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i-1]) - ord(p[i]) == 25):
                k += 1
            else:
                k = 1
            dp[p[i]] = max(dp[p[i]], k)
        #print(dp)
        return sum(dp.values())


        
