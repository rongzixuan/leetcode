"""
给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：

nums[a] + nums[b] + nums[c] == nums[d] ，且
a < b < c < d

示例 1：
输入：nums = [1,2,3,6]
输出：1
解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。

示例 2：
输入：nums = [3,3,6,4,5]
输出：0
解释：[3,3,6,4,5] 中不存在满足要求的四元组。

示例 3：
输入：nums = [1,1,1,3,5]
输出：4
解释：满足要求的 4 个四元组如下：
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5

提示：
4 <= nums.length <= 50
1 <= nums[i] <= 100

"""


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:


        # 方法一：暴力法
        # 时间复杂度：O(n^4)
        # 空间复杂度：O(1)
        n = len(nums)

        res = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            res += 1

        return res


        # 方法二：哈希表
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n)
        n = len(nums)

        from collections import defaultdict
        hash_table = defaultdict(int)

        res = 0
        for i in range(1, n):
            hash_table[nums[i - 1]] += 1
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (tmp := nums[k] - nums[i] - nums[j]) in hash_table:
                        res += hash_table[tmp]

        return res


        # 方法三：哈希表2
        # 时间复杂度：O(n^3)
        # 空间复杂度：O(n)
        n = len(nums)

        from collections import defaultdict
        hash_table = defaultdict(int)

        res = 0
        for i in range(n - 2, -1, -1):
            hash_table[nums[i + 1]] += 1
            for j in range(i - 1, -1, -1):
                for k in range(j - 1, -1, -1):
                    if (tmp := nums[k] + nums[i] + nums[j]) in hash_table:
                        res += hash_table[tmp]

        return res


        # 方法四：哈希表3
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(nums)

        from collections import defaultdict
        hash_table = defaultdict(int)

        res = 0
        for i in range(2, n):
            for j in range(i - 1):
                hash_table[nums[j] + nums[i - 1]] += 1
            for k in range(i + 1, n):
                if (tmp := nums[k] - nums[i]) in hash_table:
                    res += hash_table[tmp]

        return res


        # 方法五：哈希表4
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(nums)

        from collections import defaultdict
        hash_table = defaultdict(int)

        res = 0
        for b in range(n - 3, -1, -1):
            for d in range(b + 2, n):
                hash_table[nums[d] - nums[b + 1]] += 1
            for a in range(b):
                if (tmp := nums[a] + nums[b]) in hash_table:
                    res += hash_table[tmp]

        return res




