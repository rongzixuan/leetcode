"""
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。
MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。

当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。
每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。

请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

示例：
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true

解释： 
前两个日程安排可以添加至日历中。 第三个日程安排会导致双重预订，但可以添加至日历中。
第四个日程安排活动（5,15）不能添加至日历中，因为它会导致三重预订。
第五个日程安排（5,10）可以添加至日历中，因为它未使用已经双重预订的时间10。
第六个日程安排（25,55）可以添加至日历中，因为时间 [25,40] 将和第三个日程安排双重预订；
时间 [40,50] 将单独预订，时间 [50,55）将和第二个日程安排双重预订。

提示：
每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。
调用函数 MyCalendar.book(start, end)时， start 和 end 的取值范围为 [0, 10^9]。

"""

# 方法一：遍历
# 时间复杂度：
# __init__()：O(1)
# book()：O(n^2)
# 空间复杂度：O(n)
# n为调用次数
class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for left, right in self.overlap:
            if left < end and start < right:
                return False

        for left, right in self.calendar:
            if left < end and start < right:
                self.overlap.append((max(left, start), min(right, end)))
        self.calendar.append((start, end))
        return True


# 方法二：差分数组
# 时间复杂度：
# __init__()：O(1)
# book()：O(n^2)
# 空间复杂度：O(n)
# n为调用次数
from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.sub = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.sub[start] = self.sub.get(start, 0) + 1
        self.sub[end] = self.sub.get(end, 0) - 1
        count = 0
        for value in self.sub.values():
            count += value
            if count > 2:
                self.sub[start] = self.sub.get(start, 0) - 1
                self.sub[end] = self.sub.get(end, 0) + 1
                return False
        return True


# 方法三：线段树
# 时间复杂度：
# __init__()：O(1)
# book()：O(nlogC)
# 空间复杂度：O(nlogC)
# n为调用次数
# logC为线段树的深度
class MyCalendarTwo:
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val   # 节点最大值
            p[1] += val   # 节点懒标记
            self.tree[idx] = p
            return
        mid = (l + r) // 2
        self.update(start, end, val, l, mid, 2 * idx)
        self.update(start, end, val, mid + 1, r, 2 * idx + 1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(self.tree.get(2 * idx, (0,))[0], self.tree.get(2 * idx + 1, (0,))[0])
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start, end - 1, 1, 0, 10 ** 9, 1)
        if self.tree[1][0] > 2:
            self.update(start, end - 1, -1, 0, 10 ** 9, 1)
            return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


