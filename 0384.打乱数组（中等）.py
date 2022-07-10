"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:
Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
 
示例：

输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
 
提示：
1 <= nums.length <= 200
-10^6 <= nums[i] <= 10^6
nums 中的所有元素都是 唯一的
最多可以调用 5 * 10^4 次 reset 和 shuffle

"""

# 方法一：暴力法
# 时间复杂度：
# __init__():O(n)
# reset():O(n)
# shuffle()：O(n^2)
# 空间复杂度：O(n)
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        res = [0] * n 
        for i in range(n):
            j = random.randrange(len(self.nums))
            res[i] = self.nums.pop(j)
        self.nums = res
        return res


# 方法二：Fisher-Yates洗牌算法
# 时间复杂度：
# __init__():O(n)
# reset():O(n)
# shuffle()：O(n)
# 空间复杂度：O(n)
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = random.randrange(i, n)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


