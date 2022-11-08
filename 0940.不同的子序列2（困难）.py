"""
给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。
字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。

例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。
 
示例 1：
输入：s = "abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。

示例 2：
输入：s = "aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。

示例 3：
输入：s = "aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。

提示：
1 <= s.length <= 2000
s 仅由小写英文字母组成

"""

class Solution:
    def distinctSubseqII(self, s: str) -> int:


        # 2022/06/13
        # 方法一：动态规划 + 哈希表
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(s)
        MOD = 10 ** 9 + 7
        last = defaultdict(int)
        dp = []   # 以第i个字母结尾的子序列的个数

        for i, ch in enumerate(s):
            if i == 0:
                dp.append(1)
                last[ch] = i
                continue
            tmp = 0
            if ch not in last:
                for j in range(0, i):
                    tmp += dp[j]
                tmp += 1
            else:
                for j in range(last[ch], i):
                    tmp += dp[j]
            last[ch] = i
            dp.append(tmp)
        #print(dp)
        return sum(dp) % MOD


        # 方法二：动态规划 + 哈希表
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        n = len(s)
        MOD = 10 ** 9 + 7
        last = defaultdict(int)
        dp = [1]    # 以从0-i个字母结尾的子序列的个数

        for i, ch in enumerate(s):
            tmp = 0
            if ch not in last:
                tmp = dp[-1] * 2
            else:
                tmp = dp[-1] * 2 - dp[last[ch]] 
            last[ch] = i
            dp.append(tmp)
        #print(dp)
        return (dp[-1] - 1) % MOD


        # 2022/11/08
        # 方法一：动态规划 + 哈希表
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n)
        n = len(s)
        dp = [1] * n
        #dp[0] = 1
        ans = 0
        #mark1 = defaultdict(int)
        #mark2 = defaultdict(int)
        mark = defaultdict(list)
        for j in range(n):
            #mark2[s[j]] += 1           
            for v, arr in mark.items():
                if len(arr) == 1 and v != s[j]:
                    dp[j] += dp[arr[0]]
                else:
                    if v == s[j]:
                        dp[j] += 1
                    else:
                        for i in range(len(arr)):
                            dp[j] += (dp[arr[i]] - 1)
                        dp[j] += 1
            mark[s[j]].append(j)
            #mark1[s[j]] += 1
            #mark2 = defaultdict(int)
        #print('dp:', dp)
        #print('mark:', mark)

        ans = sum(dp)
        for k, v in mark.items():
            if len(v) > 1:
                ans -= (len(v) - 1)
        return ans % (10**9 + 7)
    
        
