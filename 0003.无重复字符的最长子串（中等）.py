"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # 方法一：滑动窗口
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        if n == 0 or n == 1:
            return n

        max_length = 1
        hash_table = set()
        i = 0

        for j in range(0, n):
            #print(i)
            if s[j] not in hash_table:
                hash_table.add(s[j])               
            else:
                hash_table.add(s[j])
                while s[i] != s[j]:                   
                    hash_table.remove(s[i])
                    i += 1
                i += 1
            max_length = max(max_length, j-i+1)
            #print(i, j)
            #print(hash_table)

        return max_length







