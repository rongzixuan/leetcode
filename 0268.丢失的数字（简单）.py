"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

示例 1：
输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 2：
输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 3：
输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

示例 4：
输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
 
提示：
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
nums 中的所有数字都 独一无二
 
进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:


        # 方法一：数学
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        res = 0
        for i in range(n):
            res += (i + 1 - nums[i])

        return res


        # 方法二：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        hash_table = set(nums)
        #print(hash_table)

        for num in range(n+1):
            if num not in hash_table:
                return num


        # 方法三：位运算
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)

        res = 0
        for num in nums:
            res |= (1 << num)

        #print(res)
        i = 0
        while res:
            if res & 1 == 0:
                return i
            i += 1
            res >>= 1

        return i


        # 方法四：排序
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i != nums[i]:
                return i

        return n


