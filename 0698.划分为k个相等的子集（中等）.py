"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

示例 2:
输入: nums = [1,2,3,4], k = 3
输出: false

提示：
1 <= k <= len(nums) <= 16
0 < nums[i] < 10000
每个元素的频率在 [1,4] 范围内

"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:


        # 方法一：回溯（记忆化搜索）（超时）
        # 时间复杂度：O(n * 2**k)
        # 空间复杂度：O(k + n)
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        print('target:', target)
        if max(nums) > target:
            return False

        count = [0] * k
        @cache
        def dfs(count, i):
            count = list(count)
            #if i == 8:
            #print(count, i)
            #if i > n:
            #    return 
            if i == n: 
                if [num == target for num in count]:
                    #print('true')
                    return True
                else:
                    return False
            for j in range(k):
                count[j] += nums[i]
                if i + 1 <= n and count[j] <= target:
                    res = dfs(tuple(count), i + 1)
                    if res:
                        return True
                count[j] -= nums[i]
            return False

        return True if dfs(tuple(count), 0) else False


        # 方法二：回溯（记忆化搜索）+ 剪枝
        # 时间复杂度：O(nlogn + n * 2**k)
        # 空间复杂度：O(k + n)
        n = len(nums)
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        #print('target:', target)
        if max(nums) > target:
            return False

        count = [0] * k
        @cache
        def dfs(count, i):
            count = list(count)
            if i == n: 
                if [num == target for num in count]:
                    #print('true')
                    return True
                else:
                    return False
            for j in range(k):
                if j> 0 and count[j] == count[j - 1]:
                    continue
                count[j] += nums[i]
                if i + 1 <= n and count[j] <= target:
                    res = dfs(tuple(count), i + 1)
                    if res:
                        return True
                count[j] -= nums[i]
            return False

        return True if dfs(tuple(count), 0) else False



        # 方法三：回溯 + 剪枝
        # 时间复杂度：O(nlogn + n * 2**k)
        # 空间复杂度：O(k + n)
        n = len(nums)
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        #print('target:', target)
        if max(nums) > target:
            return False

        count = [0] * k
        def dfs(i):
            if i == n: 
                if [num == target for num in count]:
                    #print('true')
                    return True
                else:
                    return False
            for j in range(k):
                if j> 0 and count[j] == count[j - 1]:
                    continue
                count[j] += nums[i]
                if i + 1 <= n and count[j] <= target:
                    res = dfs(i + 1)
                    if res:
                        return True
                count[j] -= nums[i]
            return False

        return True if dfs(0) else False


        # 方法四：状态压缩 + 回溯（记忆化搜索） + 剪枝
        # 时间复杂度：O(nlogn + n * 2**n)
        # 空间复杂度：O(n)
        @cache
        def dfs(state, t):
            if state == mask:
                return True
            for i, v in enumerate(nums):
                if (state >> i) & 1:
                    continue
                if t + v > s:
                    break
                if dfs(state | 1 << i, (t + v) % s):
                    return True
            return False

        s, mod = divmod(sum(nums), k)
        if mod:
            return False
        nums.sort()
        mask = (1 << len(nums)) - 1
        return dfs(0, 0)



