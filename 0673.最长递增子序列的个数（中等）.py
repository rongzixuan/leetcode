"""
给定一个未排序的整数数组，找到最长递增子序列的个数。

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
    
    
    
    
