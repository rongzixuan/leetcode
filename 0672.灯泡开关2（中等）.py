"""
房间中有 n 只已经打开的灯泡，编号从 1 到 n 。墙上挂着 4 个开关 。

这 4 个开关各自都具有不同的功能，其中：
开关 1 ：反转当前所有灯的状态（即开变为关，关变为开）
开关 2 ：反转编号为偶数的灯的状态（即 2, 4, ...）
开关 3 ：反转编号为奇数的灯的状态（即 1, 3, ...）
开关 4 ：反转编号为 j = 3k + 1 的灯的状态，其中 k = 0, 1, 2, ...（即 1, 4, 7, 10, ...）

你必须 恰好 按压开关 presses 次。每次按压，你都需要从 4 个开关中选出一个来执行按压操作。
给你两个整数 n 和 presses ，执行完所有按压之后，返回 不同可能状态 的数量。

示例 1：
输入：n = 1, presses = 1
输出：2
解释：状态可以是：
- 按压开关 1 ，[关]
- 按压开关 2 ，[开]

示例 2：
输入：n = 2, presses = 1
输出：3
解释：状态可以是：
- 按压开关 1 ，[关, 关]
- 按压开关 2 ，[开, 关]
- 按压开关 3 ，[关, 开]

示例 3：
输入：n = 3, presses = 1
输出：4
解释：状态可以是：
- 按压开关 1 ，[关, 关, 关]
- 按压开关 2 ，[关, 开, 关]
- 按压开关 3 ，[开, 关, 开]
- 按压开关 4 ，[关, 开, 开]

提示：
1 <= n <= 1000
0 <= presses <= 1000

"""

class Solution:
    def flipLights(self, n: int, presses: int) -> int:


        # 方法一：记忆化搜索
        # 时间复杂度：O(4**presses * n)
        # 空间复杂度：O(n)
        dp = [1] * n
        res = set()

        @cache
        def dfs(dp, time):
            dp = list(dp)
            nonlocal res
            #print('time, dp:', time, dp)
            if time == presses:
                res.add(tuple(dp))
                return 

            dp1 = dp.copy()
            #print('dp1 before:', dp)
            dp = [(1-x) for x in dp]
            dfs(tuple(dp), time + 1)
            #print('dp1 after:', dp)
            dp = dp1

            dp2 = dp.copy()
            #print('dp2 before:', dp)
            dp = [(1-dp[i]) if i % 2 == 1 else dp[i] for i in range(n)]
            dfs(tuple(dp), time + 1)
            #print('dp2 after:', dp)
            dp = dp2

            dp3 = dp.copy()
            #print('dp3 before:', dp)
            dp = [(1-dp[i]) if i % 2 == 0 else dp[i] for i in range(n)]
            dfs(tuple(dp), time + 1)
            #print('dp3 after:', dp)
            dp = dp3

            dp4 = dp.copy()
            #print('dp4 before:', dp)
            dp = [(1-dp[i]) if i % 3 == 0 else dp[i] for i in range(n)]
            dfs(tuple(dp), time + 1)
            #print('dp4 after:', dp)
            dp = dp4

        dfs(tuple(dp), 0)
        #print(res)
        return len(res)


        # 方法二：推理
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        if presses == 0:
            return 1
        if n == 1:
            return 2
        elif n == 2:
            if presses == 1:
                return 3
            else:
                return 4
        else:
            if presses == 1:
                return 4
            elif presses == 2:
                return 7
            else:
                return 8




            
        
