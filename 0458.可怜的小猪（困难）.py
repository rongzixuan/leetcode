"""
有 buckets 桶液体，其中 正好 有一桶含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有 minutesToTest 分钟时间来确定哪桶液体是有毒的。

喂猪的规则如下：
选择若干活猪进行喂养
可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
小猪喝完水后，必须有 minutesToDie 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
过了 minutesToDie 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
重复这一过程，直到时间用完。

给你桶的数目 buckets ，minutesToDie 和 minutesToTest ，返回在规定时间内判断哪个桶有毒所需的 最小 猪数。

示例 1：
输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
输出：5

示例 2：
输入：buckets = 4, minutesToDie = 15, minutesToTest = 15
输出：2

示例 3：
输入：buckets = 4, minutesToDie = 15, minutesToTest = 30
输出：2

提示：
1 <= buckets <= 1000
1 <= minutesToDie <= minutesToTest <= 100

"""

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:


        # 方法一：数学
        # 时间复杂度：O(1)
        # 空间复杂度：O(1)
        times = int(minutesToTest / minutesToDie) + 1
        return ceil(log(buckets) / log(times)) 

    
        # 方法二：动态规划
        # 时间复杂度：O()
        # 空间复杂度：O()
        if buckets == 1:
            return 0

        times = minutesToTest // minutesToDie        
        c = [[0] * (buckets + 1) for _ in range(buckets + 1)]  # 组合计算
        c[0][0] = 1

        # dp[i][j]表示用i只小猪，经过j轮能判断出的最多的桶的数目
        dp = [[0] * (times + 1) for _ in range(buckets + 1)] 
        for i in range(buckets + 1):
            dp[i][0] = 1
        for i in range(times + 1):
            dp[0][i] = 1

        for i in range(1, buckets + 1):
            c[i][0] = 1
            c[i][i] = 1
            for k in range(1, i):
                c[i][k] = c[i-1][k] + c[i-1][k-1]
            for j in range(1, times + 1):
                for k in range(i + 1):
                    dp[i][j] += dp[k][j-1] * c[i][k]
                if dp[i][j] >= buckets:
                    return i

        return 0



