"""
给你两个整数 n 和 maxValue ，用于描述一个 理想数组 。

对于下标从 0 开始、长度为 n 的整数数组 arr ，如果满足以下条件，则认为该数组是一个 理想数组 ：
每个 arr[i] 都是从 1 到 maxValue 范围内的一个值，其中 0 <= i < n 。
每个 arr[i] 都可以被 arr[i - 1] 整除，其中 0 < i < n 。

返回长度为 n 的 不同 理想数组的数目。由于答案可能很大，返回对 109 + 7 取余的结果。

示例 1：
输入：n = 2, maxValue = 5
输出：10
解释：存在以下理想数组：
- 以 1 开头的数组（5 个）：[1,1]、[1,2]、[1,3]、[1,4]、[1,5]
- 以 2 开头的数组（2 个）：[2,2]、[2,4]
- 以 3 开头的数组（1 个）：[3,3]
- 以 4 开头的数组（1 个）：[4,4]
- 以 5 开头的数组（1 个）：[5,5]
共计 5 + 2 + 1 + 1 + 1 = 10 个不同理想数组。

示例 2：
输入：n = 5, maxValue = 3
输出：11
解释：存在以下理想数组：
- 以 1 开头的数组（9 个）：
   - 不含其他不同值（1 个）：[1,1,1,1,1] 
   - 含一个不同值 2（4 个）：[1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - 含一个不同值 3（4 个）：[1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- 以 2 开头的数组（1 个）：[2,2,2,2,2]
- 以 3 开头的数组（1 个）：[3,3,3,3,3]
共计 9 + 1 + 1 = 11 个不同理想数组。
 
提示：
2 <= n <= 10^4
1 <= maxValue <= 10^4

"""

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        
        
        # 方法一：回溯（超时）
        # 时间复杂度：O(n * maxValue)
        # 空间复杂度：O(n)
        """used = defaultdict(int)
        def dfs(index, num):
            #print('index, num:', index, num)
            if num > maxValue:
                return 0
            if index == n and num <= maxValue:
                #print('yes, index, num:', index, num)
                return 1
            if index == n:
                return 0
            res = 0
            for i in range(1, maxValue + 1):
                #print('i:', i)
                if num * i > maxValue:
                    break
                res += dfs(index + 1, num * i)
            return res
        
        ans = 0
        for num in range(1, maxValue + 1):
            ans += dfs(1, num)
        return ans % (10 ** 9 + 7)"""


        # 方法二：组合数学
        # 时间复杂度：O()
        # 空间复杂度：O()
        MX_K = 13
        MOD, MX = 10 ** 9 + 7, 10 ** 4 + MX_K

        ks = [[] for _ in range(MX)]  # ks[x] 为 x 分解质因数后，每个质因数的个数列表
        for i in range(2, MX):
            p, x = 2, i
            while p * p <= x:
                if x % p == 0:
                    k = 0
                    while x % p == 0:
                        k += 1
                        x //= p
                    ks[i].append(k)
                p += 1
            if x > 1:
                ks[i].append(1)
        print(ks)
        print(ks[12])

        c = [[0] * (MX_K + 1) for _ in range(MX)]  # 组合数
        c[0][0] = c[1][0] = c[1][1] = 1
        for i in range(2, MX):
            c[i][0] = 1
            for j in range(1, min(i, MX_K) + 1):
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

        ans = 0
        for x in range(1, maxValue + 1):
            mul = 1
            for k in ks[x]:
                mul = mul * c[n + k - 1][k] % MOD
            ans += mul
        return ans % MOD



