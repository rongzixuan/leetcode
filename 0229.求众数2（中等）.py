"""
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:


        # 方法一：哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        if n == 1:
            return [nums[0]]

        from collections import defaultdict
        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] += 1

        res = []
        #print(n // 3)
        for k, v in hash_table.items():
            if v > n // 3:
                res.append(k)

        return res


        # 方法二：摩尔投票法
        # 时间复杂度：O(1)
        # 空间复杂度：O(n)
        n = len(nums)
        if n == 1:
            return [nums[0]]

        num1, num2 = 0, 0
        vote1, vote2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == num1:
                vote1 += 1
            elif vote2 > 0 and num == num2:
                vote2 += 1
            elif vote1 == 0:
                num1 = num
                vote1 += 1
            elif vote2 == 0:
                num2 = num
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1
        #print('vote1, vote2:', vote1, vote2)
        #print('num1, num2:', num1, num2)

        count1, count2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == num1:
                count1 += 1
            elif vote2 > 0 and num == num2:
                count2 += 1
        #print('count1, count2:', count1, count2)

        res = []
        if count1 > n // 3:
            res.append(num1)
        if count2 > n // 3:
            res.append(num2)

        return res


