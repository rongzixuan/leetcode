"""
给你一个数组 nums ，请你完成两类查询。

其中一类查询要求 更新 数组 nums 下标对应的值
另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
实现 NumArray 类：

NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值 更新 为 val
int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
 

示例 1：

输入：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
[null, 9, null, 8]

解释：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
 

提示：
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
调用 update 和 sumRange 方法次数不大于 3 * 10^4 

"""


# 方法一：模拟（超时）
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right + 1])



# 方法二：分块处理
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.m = int(self.n ** 0.5)
        self.sums = [0] * ((self.n + self.m - 1) // self.m)

        for i in range(self.n):
            self.sums[i // self.m] += nums[i]

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.m] += (val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        block1, block2 = left // self.m, right // self.m
        if block1 == block2:  # 在同一个分块里
            return sum(self.nums[left: right + 1])
        else:
            return sum(self.nums[left: (block1 * self.m + self.m)]) \
                    + sum(self.sums[block1 + 1 : block2]) \
                    + sum(self.nums[block2 * self.m: (right + 1)]) 


# 方法三：线段树
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.segment_tree = [0] * (self.n * 4)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start == end:
            self.segment_tree[node] = nums[start]
            return 
        mid = start + (end - start) // 2
        self.build(nums, node * 2 + 1, start, mid)
        self.build(nums, node * 2 + 2, mid + 1, end)
        self.segment_tree[node] = self.segment_tree[node * 2 + 1] + self.segment_tree[node * 2 + 2]

    def change(self, index, val, node, start, end):
        if start == end:
            self.segment_tree[node] = val
            return 
        mid = start + (end - start) // 2
        if index <= mid:
            self.change(index, val, node * 2 + 1, start, mid)
        else:
            self.change(index, val, node * 2 + 2, mid + 1, end)
        self.segment_tree[node] = self.segment_tree[node * 2 + 1] + self.segment_tree[node * 2 + 2]

    def range(self, left, right, node, start, end):
        if left == start and right == end:
            return self.segment_tree[node]
        mid = start + (end - start) // 2
        if right <= mid:
            return self.range(left, right, node * 2 + 1, start, mid)
        elif left > mid:
            return self.range(left, right, node * 2 + 2, mid + 1, end)
        return self.range(left, mid, node * 2 + 1, start, mid) + self.range(mid + 1, right, node * 2 + 2, mid + 1, end)

    def update(self, index: int, val: int) -> None:
        self.change(index, val, 0, 0, self.n - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.range(left, right, 0, 0 , self.n - 1)


# 方法四：树状数组
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i, num in enumerate(nums, 1):
            self.add(i, num) 

    def add(self, i, num):
        while i <= self.n:
            self.tree[i] += num   
            i += (i & (-i))  
            
    def prefixSum(self, i):
        res = 0
        while i:
            res += self.tree[i]
            #i -= (i & (-i))
            i &= (i - 1)
        return res

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


