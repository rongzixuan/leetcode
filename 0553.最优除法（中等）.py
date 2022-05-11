"""
给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。
但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。

示例：
输入: [1000,100,10,2]
输出: "1000/(100/10/2)"
解释:
1000/(100/10/2) = 1000/((100/10)/2) = 200
但是，以下加粗的括号 "1000/((100/10)/2)" 是冗余的，
因为他们并不影响操作的优先级，所以你需要返回 "1000/(100/10/2)"。

其他用例:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

说明:
输入数组的长度在 [1, 10] 之间。
数组中每个元素的大小都在 [2, 1000] 之间。
每个测试用例只有一个最优除法解。

"""


class Node:
    def __init__(self):
        self.minVal = float('inf')
        self.maxVal = float('-inf')
        self.maxStr = ""
        self.minStr = ""

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:


        # 方法一：贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 1:
            return str(nums[0]) 
        elif n == 2:
            return str(nums[0]) + '/' + str(nums[1])

        res = str(nums[0]) + '/('
        for i in range(1, n):
            res += str(nums[i]) + '/'

        res = res[: -1] + ')'
        return res


        # 方法二：动态规划
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n^2)
        n = len(nums)

        dp = [[Node() for _ in range(n)] for _ in range(n)]   # dp[i][j]表示
        for i in range(n):
            dp[i][i].minVal = nums[i]
            dp[i][i].maxVal = nums[i]
            dp[i][i].minStr = str(nums[i])
            dp[i][i].maxStr = str(nums[i])
        #print(dp)

        for length in range(n):
            for i in range(n - length):
                for k in range(i, i + length):
                    if dp[i][i + length].maxVal < dp[i][k].maxVal / dp[k + 1][i + length].minVal:
                        dp[i][i + length].maxVal = dp[i][k].maxVal / dp[k + 1][i + length].minVal
                        if k + 1 == i + length:
                            dp[i][i + length].maxStr = dp[i][k].maxStr + "/" + dp[k + 1][i + length].minStr
                        else:
                            dp[i][i + length].maxStr = dp[i][k].maxStr + "/(" + dp[k + 1][i + length].minStr + ")"
                    if dp[i][i + length].minVal > dp[i][k].minVal / dp[k + 1][i + length].maxVal:
                        dp[i][i + length].minVal = dp[i][k].minVal / dp[k + 1][i + length].maxVal
                        if k + 1 == i + length:
                            dp[i][i + length].minStr = dp[i][k].minStr + "/" + dp[k + 1][i + length].maxStr
                        else:
                            dp[i][i + length].minStr = dp[i][k].minStr + "/(" + dp[k + 1][i + length].maxStr + ")"

        return dp[0][n - 1].maxStr





