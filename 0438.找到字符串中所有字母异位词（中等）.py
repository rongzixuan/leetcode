"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。 

提示:
1 <= s.length, p.length <= 3 * 10^4
s 和 p 仅包含小写字母

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:


        # 方法一：滑动窗口
        # 时间复杂度：O(m)
        # 空间复杂度：O(C)，C = 26
        m, n = len(s), len(p)
        if m < n:
            return []

        table_s = [0] * 26
        table_p = [0] * 26
        for i in range(n):
            table_s[ord(s[i]) - ord('a')] += 1
            table_p[ord(p[i]) - ord('a')] += 1
        #print(table_s)
        #print(table_p)

        res = [] if table_p != table_s else [0]
        
        for i in range(n, m):
            #print(i, s[i], s[i-n])
            table_s[ord(s[i]) - ord('a')] += 1
            table_s[ord(s[i-n]) - ord('a')] -= 1
            #print(table_s)
            if table_p == table_s:
                #print(i-n+1)
                res.append(i-n+1)

        return res


        # 方法二：滑动窗口2
        # 时间复杂度：O(m)
        # 空间复杂度：O(C)，C = 26
        m, n = len(s), len(p)
        if m < n:
            return []

        table = [0] * 26
        for i in range(n):
            table[ord(s[i]) - ord('a')] += 1
            table[ord(p[i]) - ord('a')] -= 1
        #print(table)

        diff = [t != 0 for t in table].count(True)
        #print(diff)
        res = [] if diff else [0]
        
        for i in range(n, m):
            #print(i, s[i], s[i-n])         
            if table[ord(s[i]) - ord('a')] == 0:
                diff += 1
            elif table[ord(s[i]) - ord('a')] == -1:
                diff -= 1
            table[ord(s[i]) - ord('a')] += 1
                           
            if table[ord(s[i-n]) - ord('a')] == 0:
                diff += 1   
            elif table[ord(s[i-n]) - ord('a')] == 1:
                diff -= 1   
            table[ord(s[i-n]) - ord('a')] -= 1
            #print(table)
            #print(diff)
            if diff == 0:
                #print(i-n+1)
                res.append(i-n+1)

        return res


    
    
    

