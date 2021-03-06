"""
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。

示例 1：
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"

示例 2：
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"

提示：
1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s 和 dictionary[i] 仅由小写英文字母组成

"""


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:


        # 方法一：双指针
        # 时间复杂度：O(n*(d+n))，其中d为dic长度
        # 空间复杂度：O(1)
        m, n = len(s), len(dictionary)
        res = ''

        for i in range(n):
            dic = dictionary[i]
            p1 = p2 = 0
            while p2 < len(dic) and p1 < m:
                if s[p1] == dic[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    while p1 < m and s[p1] != dic[p2]:
                        p1 += 1

            if p1 == m and p2 != len(dic):
                continue
            else:
                res = dic if len(dic) > len(res) or(len(dic) == len(res) and dic < res) else res

        return res


        # 方法二：排序 + 双指针
        # 时间复杂度：O(n*(d+n))，其中d为dic长度
        # 空间复杂度：O(1)
        dictionary.sort()
        m, n = len(s), len(dictionary)
        res = ''

        for i in range(n):
            dic = dictionary[i]
            p1 = p2 = 0
            while p2 < len(dic) and p1 < m:
                if s[p1] == dic[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    while p1 < m and s[p1] != dic[p2]:
                        p1 += 1

            if p1 == m and p2 != len(dic):
                continue
            else:
                res = dic if len(dic) > len(res) else res

        return res


        # 方法三：动态规划
        # 时间复杂度：O(n + m * d)，其中d为dic长度
        # 空间复杂度：O(n)， n为字符串s的长度
        m, n = len(dictionary), len(s)
        dp = [[0] * 26 for _ in range(n)]
        dp.append([n] * 26)
        #print(dp)

        # dp[i][j]表示从i开始字符j第一次出现的位置
        for i in range(n-1, -1, -1):
            for j in range(26):
                if s[i] == chr(97 + j):
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i+1][j]
        #print(dp)

        res = ""
        for dic in dictionary:
            j = 0
            match = True
            for i in range(len(dic)):
                if dp[j][ord(dic[i])-97] == n:
                    match = False
                    break
                j = dp[j][ord(dic[i])-97] + 1
            #print(match)
            if match:
                if len(dic) > len(res) or (len(dic) == len(res) and dic < res):
                    res = dic

        return res






