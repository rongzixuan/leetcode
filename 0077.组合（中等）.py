"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        # 方法一：回溯
        # 时间复杂度：O(n * k * k!)
        # 空间复杂度：O(1)
        if n == 1:
            return [[1]]

        ans = []
        res = []
        def backtrace(index):
            if index == k:
                ans.append(res[:])
                return 

            for i in range(1, n+1):
                if i not in res and (index == 0 or i > res[-1]):
                    res.append(i)
                    backtrace(index + 1)
                    res.pop(-1)

        backtrace(0)
        return ans


        # 方法二：回溯2
        # 时间复杂度：O(n * k!)
        # 空间复杂度：O(1)
        if n == 1:
            return [[1]]

        ans = []
        res = []
        def backtrace(index):
            if len(res) == k:
                ans.append(res[:])
                return 

            for i in range(index+1, n+1):
                res.append(i)
                backtrace(i)
                res.pop(-1)

        backtrace(0)
        return ans

    
    
