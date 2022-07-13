"""
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。
如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。

再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。

"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:


        # 方法一：差分 + 哈希表 + 动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(nums)
        if n < 3:
            return 0

        hash_table = [defaultdict(list) for _ in range(n)]
        #print('hash_table:', hash_table)
        #print(hash_table[0])
        #print('------')
        count = 0

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                diff = nums[i] - nums[j]
                if hash_table[i][diff]:
                    hash_table[i][diff] += (hash_table[j][diff] or 0) + 1
                else:
                    hash_table[i][diff] = (hash_table[j][diff] or 0) + 1                    
                #print(i, j, diff, hash_table)
                if hash_table[j][diff] :
                    count += hash_table[j][diff] 

        return count



    
