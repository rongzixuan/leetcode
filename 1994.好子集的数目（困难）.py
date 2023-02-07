"""
给你一个整数数组 nums 。如果 nums 的一个子集中，所有元素的乘积可以表示为一个或多个 互不相同的质数 的乘积，那么我们称它为 好子集 。

比方说，如果 nums = [1, 2, 3, 4] ：
[2, 3] ，[1, 2, 3] 和 [1, 3] 是 好 子集，乘积分别为 6 = 2*3 ，6 = 2*3 和 3 = 3 。
[1, 4] 和 [4] 不是 好 子集，因为乘积分别为 4 = 2*2 和 4 = 2*2 。

请你返回 nums 中不同的 好 子集的数目对 109 + 7 取余 的结果。

nums 中的 子集 是通过删除 nums 中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视为不同的子集。

示例 1：
输入：nums = [1,2,3,4]
输出：6
解释：好子集为：
- [1,2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [1,2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [1,3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。

示例 2：
输入：nums = [4,2,3,15]
输出：5
解释：好子集为：
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同质数 2 和 3 的乘积。
- [2,15]：乘积为 30 ，可以表示为互不相同质数 2，3 和 5 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [15]：乘积为 15 ，可以表示为互不相同质数 3 和 5 的乘积。
 
提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 30

"""


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:


        # 方法一：压缩状态动态规划
        # 时间复杂度：
        # 空间复杂度：
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        MOD = 10 ** 9 + 7
       
        from collections import Counter
        counter = Counter(nums)
        #print('counter:', counter)
        #print('counter[1]:', counter[1])
        dp = [0] * (1 << len(primes))
        dp[0] = pow(2, counter[1], MOD)
        #print('len(dp):', len(dp))
        #print('dp:', dp)

        for i, cnt in counter.items():
            if i == 1:
                continue

            tmp_i = i
            flag = True
            subset = 0
            for j in range(len(primes)):
                if tmp_i % (primes[j] * primes[j]) == 0:
                    flag = False
                    break
                if tmp_i % primes[j] == 0:
                    subset |= (1 << j)

            if not flag:
                continue

            # 动态规划
            for mask in range((1 << len(primes)) - 1, 0, -1):
                if (mask & subset) == subset:
                    dp[mask] = (dp[mask] + dp[mask ^ subset] * cnt) % MOD

        return sum(dp[1: ]) % MOD







