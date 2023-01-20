"""
给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。

MK 平均值 按照如下步骤计算：
如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。
从这个容器中删除最小的 k 个数和最大的 k 个数。
计算剩余元素的平均值，并 向下取整到最近的整数 。

请你实现 MKAverage 类：
MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。
void addElement(int num) 往数据流中插入一个新的元素 num 。
int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。
 

示例 1：

输入：
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
输出：
[null, null, null, -1, null, 3, null, null, null, 5]

解释：
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // 当前元素为 [3]
obj.addElement(1);        // 当前元素为 [3,1]
obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10);       // 当前元素为 [3,1,10]
obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
                          // 删除最小以及最大的 1 个元素后，容器为 [3]
                          // [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5);        // 当前元素为 [3,1,10,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
                          // 删除最小以及最大的 1 个元素后，容器为 [5]
                          // [5] 的平均值等于 5/1 = 5 ，故返回 5
 
提示：
3 <= m <= 10^5
1 <= k*2 < m
1 <= num <= 10^5
addElement 与 calculateMKAverage 总操作次数不超过 10^5 次。

"""

# 方法一：有序队列（超时）
# 时间复杂度：
# addELement(logm)：
# calculateMKAverage(k)：
# 空间复杂度：O(m)
from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue_m = []
        self.queue_k = []
        self.queue_lower = SortedList()
        self.queue_upper = SortedList()
        self.sum1, self.sum2, self.sum3 = 0, 0, 0

    def addElement(self, num: int) -> None:
        if len(self.queue_m) >= self.m:
            pre_m = self.queue_m.pop(0)
            self.sum1 -= pre_m
        self.queue_m.append(num)
        self.sum1 += num          

        if len(self.queue_k) >= self.k:
            pre_k = self.queue_k.pop(0)
        self.queue_k.append(num)

        if len(self.queue_lower) >= self.m:
            self.queue_lower.remove(pre_m)
        self.queue_lower.add(num)

        if len(self.queue_upper) >= self.m:
            self.queue_upper.remove(-pre_m)
        self.queue_upper.add(-num)

    def calculateMKAverage(self) -> int:
        #print('self.queue_m:', self.queue_m)
        #print('self.queue_k:', self.queue_k)
        #print('self.queue_lower:', self.queue_lower)
        #print('self.queue_upper:', self.queue_upper)
        if len(self.queue_m) < self.m:
            return -1
        else:
            sum_lower, sum_upper = 0, 0
            for i in range(self.k):
                sum_lower += self.queue_lower[i]
                sum_upper -= self.queue_upper[i]
            return (self.sum1 - sum_lower - sum_upper) // (self.m - 2 * self.k)


# 方法二：有序队列
# 时间复杂度：
# addELement(logm)：
# calculateMKAverage(1)：
# 空间复杂度：O(m)
from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.s = 0
        self.q = deque()
        self.lo = SortedList()
        self.mid = SortedList()
        self.hi = SortedList()

    def addElement(self, num: int) -> None:
        if not self.lo or num <= self.lo[-1]:
            self.lo.add(num)
        elif not self.hi or num >= self.hi[0]:
            self.hi.add(num)
        else:
            self.mid.add(num)
            self.s += num
        self.q.append(num)
        if len(self.q) > self.m:
            x = self.q.popleft()
            if x in self.lo:
                self.lo.remove(x)
            elif x in self.hi:
                self.hi.remove(x)
            else:
                self.mid.remove(x)
                self.s -= x
        while len(self.lo) > self.k:
            x = self.lo.pop()
            self.mid.add(x)
            self.s += x
        while len(self.hi) > self.k:
            x = self.hi.pop(0)
            self.mid.add(x)
            self.s += x
        while len(self.lo) < self.k and self.mid:
            x = self.mid.pop(0)
            self.lo.add(x)
            self.s -= x
        while len(self.hi) < self.k and self.mid:
            x = self.mid.pop()
            self.hi.add(x)
            self.s -= x

    def calculateMKAverage(self) -> int:
        return -1 if len(self.q) < self.m else self.s // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

