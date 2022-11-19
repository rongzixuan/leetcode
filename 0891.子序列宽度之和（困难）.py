"""
一个序列的 宽度 定义为该序列中最大元素和最小元素的差值。
给你一个整数数组 nums ，返回 nums 的所有非空 子序列 的 宽度之和 。由于答案可能非常大，请返回对 109 + 7 取余 后的结果。

子序列 定义为从一个数组里删除一些（或者不删除）元素，但不改变剩下元素的顺序得到的数组。例如，[3,6,2,7] 就是数组 [0,3,1,6,2,2,7] 的一个子序列。

示例 1：
输入：nums = [2,1,3]
输出：6
解释：子序列为 [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3] 。
相应的宽度是 0, 0, 0, 1, 1, 2, 2 。
宽度之和是 6 。

示例 2：
输入：nums = [2]
输出：0
 
提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

"""

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:


        # 方法一：数学（超时）
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        MOD = 10 ** 9 + 7
        n = len(nums)
        if max(nums) == min(nums):
            return 0

        from collections import Counter
        from sortedcontainers import SortedDict
        count = SortedDict(Counter(nums))
        #print(count)

        ans = 0
        m = len(count)
        i = 0
        pre = 0
        for k, v in count.items():
            #print(k, v)
            #ans = (ans + k * (2**pre - 1) * (2**v - 1)) % MOD           # 以k为最大值的个数
            #print('ans:', ans)
            #ans = (ans - k * (2**(n - pre - v) - 1) * (2**v - 1)) % MOD # 以k为最小值的个数
            ans = (ans + k * (2**pre - 2**(n - pre - v)) * (2**v - 1)) % MOD   # 合并
            #print('ans:', ans)
            i += 1
            pre += v
        return ans


        # 方法二：数学
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        MOD = 10 ** 9 + 7
        n = len(nums)
        if max(nums) == min(nums):
            return 0

        from collections import Counter
        from sortedcontainers import SortedDict
        count = SortedDict(Counter(nums))
        #print(count)

        ans = 0
        m = len(count)
        i = 0
        pre = 1
        aft = 2**n
        for k, v in count.items():
            #print(k, v)  
            aft //= 2**v   
            #ans = (ans + k * (2**pre - 1) * (2**v - 1)) % MOD           # 以k为最大值的个数
            #print('ans:', ans)
            #ans = (ans - k * (2**(n - pre - v) - 1) * (2**v - 1)) % MOD # 以k为最小值的个数
            #ans = (ans + k * (2**pre - 2**(n - pre - v)) * (2**v - 1)) % MOD   # 合并
            ans = (ans + k * (pre - aft) * (2**v - 1)) % MOD   # 合并
            #print('ans:', ans)
            i += 1
            pre *= 2**v       
        return ans


        # 方法三：数学
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        MOD = 10 ** 9 + 7
        n = len(nums)
        if max(nums) == min(nums):
            return 0
        nums.sort()

        ans = 0
        pre = 1
        aft = 2**n
        for i, num in enumerate(nums):
            aft //= 2  
            ans = (ans + num * (pre - aft)) % MOD   # 合并
            #print('ans:', ans)
            i += 1
            pre *= 2      
        return ans
        

        # 方法四：数学
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        nums.sort()
        res = 0
        MOD = 10 ** 9 + 7
        x, y = nums[0], 2
        for j in range(1, len(nums)):
            res = (res + nums[j] * (y - 1) - x) % MOD
            x = (x * 2 + nums[j]) % MOD
            y = y * 2 % MOD
        return (res + MOD) % MOD


        # 方法五：数学
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [0] * n
        pow2[0] = 1
        for i in range(1, n):
            pow2[i] = pow2[i - 1] * 2 % MOD  # 预处理 2 的幂次
        return sum((pow2[i] - pow2[-1 - i]) * x
                   for i, x in enumerate(nums)) % MOD





