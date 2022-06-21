"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:


        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        from collections import defaultdict
        hash_table = defaultdict(int)

        for num in nums:
            hash_table[num] += 1

        res = []
        for k, v in hash_table.items():
            if v == 1:
                res.append(k)

        return res


        # 方法二：位运算
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        res = 0
        for num in nums:
            res ^= num
        #print(res)
        #print(bin(-1))

        index = res & (-res)  # 最后一次出现1的位置
        num1, num2 = 0, 0
        for num in nums:
            if num & index:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


