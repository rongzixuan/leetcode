"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        # 方法一：回溯
        # 时间复杂度：O(3^m * 4^n)，其中m、n为按键中对应个数为3个、4个的按键个数
        # 空间复杂度：O(m + n)
        n = len(digits)
        if n == 0:
            return []

        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = []
        res = []
        def backtrace(index):
            if index == n:
                ans.append("".join(res))
            else:
                for ch in phoneMap[digits[index]]:
                    res.append(ch)
                    backtrace(index + 1)
                    res.pop()

        backtrace(0)
        return ans



    
