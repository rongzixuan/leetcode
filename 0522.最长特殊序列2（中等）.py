"""
给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。

特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
 s 的 子序列可以通过删去字符串 s 中的某些字符实现。
例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。
 
示例 1：
输入: strs = ["aba","cdc","eae"]
输出: 3

示例 2:
输入: strs = ["aaa","aaa","aa"]
输出: -1
 
提示:
2 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] 只包含小写英文字母

"""

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:


        # 方法一：枚举
        # 时间复杂度：O(n^2 * l)
        # 空间复杂度：O(1)
        # l为str的平均长度
        def is_subseq(str_i: str, str_j: str) -> bool:
            i = j = 0
            while i < len(str_i) and j < len(str_j):
                if str_i[i] == str_j[j]:
                    i += 1
                j += 1
            return i == len(str_i)
        
        ans = -1
        for i, str_i in enumerate(strs):
            check = True
            for j, str_j in enumerate(strs):
                if i != j and is_subseq(str_i, str_j):
                    check = False
                    break
            if check:
                ans = max(ans, len(str_i))
        
        return ans



