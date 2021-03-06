"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

"""

class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        if n == 0:
            return 0
        count = n
            
        # 方法一：动态规划
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = 2  
                        count += 1 
                        #print(i, j)         
                    else:
                        dp[i][j] = 0
                elif s[i] == s[j] and dp[i+1][j-1] > 0:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    if dp[i][j] > 2:
                        #print(i, j)
                        count += 1
                else:
                    #dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    dp[i][j] = 0
                    
        return count


        # 方法二：动态规划
        count = n
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if i + 1 == j and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                elif j - i > 1 and dp[i+1][j-1] == True and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1

        return count


        # 方法三：中心扩展法
        count = 0
        for i in range(n):
            for j in range(i, i+2):
                #print('i, j-1:', i, j)
                left, right = i, j
                while left >= 0 and right < n: 
                    #print('left, right-2:', left, right)
                    if s[left] == s[right]:
                        count += 1
                        left -= 1
                        right += 1
                    else:
                        break

        return count


        # 方法四：中心扩展法2
        count = 0

        for i in range(2 * n + 1):
            left = i // 2
            right = i // 2 + i % 2
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break

        return count



