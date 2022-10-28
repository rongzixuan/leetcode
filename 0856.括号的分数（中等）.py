"""
给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 
示例 1：
输入： "()"
输出： 1

示例 2：
输入： "(())"
输出： 2

示例 3：
输入： "()()"
输出： 2

示例 4：
输入： "(()(()))"
输出： 6

提示：
S 是平衡括号字符串，且只含有 ( 和 ) 。
2 <= S.length <= 50

"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:


        # 方法一：栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(s)
        stack = []
        ans = 0
        count1, count2 = 0, 0

        for i, ch in enumerate(s):
            tmp = 0
            if ch == '(':
                stack.append("(")
            else:
                stack.pop()
                if s[i - 1] == "(":
                    length = len(stack)
                    ans += 2 ** (length)
        return ans


        # 方法二：递归
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(s)
        if n == 2:
            return 1
        bal = 0
        for i, c in enumerate(s):
            bal += 1 if c == '(' else -1
            if bal == 0:
                if i == n - 1:
                    return 2 * self.scoreOfParentheses(s[1:-1])
                return self.scoreOfParentheses(s[:i + 1]) + self.scoreOfParentheses(s[i + 1:])







