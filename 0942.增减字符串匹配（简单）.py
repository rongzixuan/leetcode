"""
由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:

如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I' 
如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D' 
给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。


示例 1：
输入：s = "IDID"
输出：[0,4,1,3,2]

示例 2：
输入：s = "III"
输出：[0,1,2,3]

示例 3：
输入：s = "DDI"
输出：[3,2,0,1]
 
提示：
1 <= s.length <= 1^05
s 只包含字符 "I" 或 "D"

"""

class Solution:
    def diStringMatch(self, s: str) -> List[int]:


        # 方法一：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(s)
        res = [0] * (n + 1)
            
        #count1, count2 = sum([ch == 'I' for ch in s]), sum([ch == 'D' for ch in s])
        #print(count1, count2)
        res[0] = 0 if s[0] == 'I' else n
        candidate_set = [i for i in range(1, n + 1)] if s[0] == 'I' else [i for i in range(0, n)]

        for i in range(n):
            if s[i] == 'I':
                res[i + 1] = candidate_set.pop(0) if i + 1 < n and s[i + 1] == 'I' else candidate_set.pop()
            elif s[i] == 'D':
                res[i + 1] = candidate_set.pop() if i + 1 < n and s[i + 1] == 'D' else candidate_set.pop(0)

        return res


        # 方法二：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        lo = 0
        hi = n = len(s)
        perm = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = lo
                lo += 1
            else:
                perm[i] = hi
                hi -= 1
        perm[n] = lo  # 最后剩下一个数，此时 lo == hi
        return perm







