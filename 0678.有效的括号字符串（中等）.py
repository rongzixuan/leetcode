"""
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。

"""

class Solution:
    def checkValidString(self, s: str) -> bool:


        # 方法一：栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        stack1 = []
        stack2 = []
        n = len(s)
        if n == 1:
            if s[0] != '*':
                return False
            elif s[0] == '*':
                return True

        count = 0
        for i in range(n):
            if s[i] == '(':
                stack1.append(i)
            elif s[i] == ')':
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False
            elif s[i] == '*':
                stack2.append(i)

        #print(stack1)
        #print(stack2)
        if not stack1 and not stack2:
            return True
        elif len(stack1) > len(stack2):
            return False
        elif len(stack1) > 0 and len(stack2) > 0 and stack1[-1] > stack2[-1]:
            return False
        else:
            n1, n2 = len(stack1), len(stack2)
            while stack1:
                if stack1[-1] > stack2[-1]:
                    return False
                else:
                    stack1.pop()
                    stack2.pop()
            return True


        # 方法二：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        left_min = left_max = 0
        n = len(s)
        #print('n:', n)
        if n == 1:
            if s[0] != '*':
                return False
            elif s[0] == '*':
                return True

        for i in range(n):
            if s[i] == '(':
                left_min += 1
                left_max += 1
            elif s[i] == ')':
                left_min = max(left_min - 1, 0)
                left_max -= 1
            elif s[i] == '*':
                left_min = max(left_min - 1, 0)
                left_max += 1

            if left_max < 0:
                #print('2')
                return False

        #print(left_min, left_max)
        return left_min == 0


        # 方法三：动态规划
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n^2)
        n = len(s)
        #print('n:', n)
        if n == 1:
            if s[0] != '*':
                return False
            elif s[0] == '*':
                return True

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1:
                if s[i] == '(' and s[i+1] == ')':
                    dp[i][i+1] = True
                elif s[i] == '*' and s[i+1] == ')':
                    dp[i][i+1] = True
                elif s[i] == '(' and s[i+1] == '*':
                    dp[i][i+1] = True
                elif s[i] == '*' and s[i+1] == '*':
                    dp[i][i+1] = True

        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                #print(i, j)
                if dp[i+1][j-1] == True:
                    if s[i] == '*' and s[j] == '*':
                        dp[i][j] = True
                        #continue
                    elif s[i] == '*' and s[j] == ')':
                        dp[i][j] = True
                        #continue
                    elif s[i] == '(' and s[j] == ')':
                        dp[i][j] = True
                        #continue
                    elif s[i] == '(' and s[j] == '*':
                        dp[i][j] = True
                        #continue
                for k in range(i, j):
                    if dp[i][k] == True and dp[k+1][j] == True and dp[i][j] == False:
                        dp[i][j] = True
                        #continue
                #dp[i][j] = False


        #print(dp)
        return dp[0][n-1] == True


