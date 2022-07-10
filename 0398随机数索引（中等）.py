"""
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

示例:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);

"""


# 方法一：哈希表
# 时间复杂度：O(n)
# 空间复杂度：O(n)
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.count = defaultdict(list)
        for i, num in enumerate(nums):
            self.count[num].append(i)

    def pick(self, target: int) -> int:
        length = len(self.count[target])
        index = random.randint(0, length - 1)
        return self.count[target][index]
        

# 方法二：水塘抽样算法
# 时间复杂度：O(1)
# 空间复杂度：O(1)
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = 0
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if randint(0, count - 1) == 0:
                    ans = i

        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


