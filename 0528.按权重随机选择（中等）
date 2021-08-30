"""
给定一个正整数数组 w ，其中 w[i] 代表下标 i 的权重（下标从 0 开始），请写一个函数 pickIndex ，它可以随机地获取下标 i，选取下标 i 的概率与 w[i] 成正比。

例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。

也就是说，选取下标 i 的概率为 w[i] / sum(w) 。

"""

class Solution:


    # 方法一：前缀和 + 二分法
    # 时间复杂度：
    # __init__函数：O(n)
    # pickIndex函数：O(logn)，调用bisection函数
    # bisection函数：O(logn)
    # 空间复杂度：O(n)
    def __init__(self, w: List[int]):
        #print(w)
        self.nums = w

        self.pre_sum = []
        self.nums_sum = 0
        for num in self.nums:
            self.nums_sum += num
            self.pre_sum.append(self.nums_sum)
        #print('pre_sum:', self.pre_sum)
        #print('nums_sum:', self.nums_sum)


    def bisection(self, random_num, n):
        nums = self.nums
        pre_sum = self.pre_sum

        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if pre_sum[mid] == random_num:
                return mid
            elif pre_sum[mid] < random_num:
                left = mid + 1
            elif pre_sum[mid] > random_num:
                right = mid - 1
        return left


    def pickIndex(self) -> int:
        nums = self.nums
        pre_sum = self.pre_sum
        nums_sum = self.nums_sum

        n = len(nums)
        if n == 1:
            return 0

        random_num = random.randint(1, nums_sum)
        print('random_num:', random_num)
        return self.bisection(random_num, n)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
