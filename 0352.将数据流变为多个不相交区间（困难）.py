"""
 给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。

实现 SummaryRanges 类：
SummaryRanges() 使用一个空数据流初始化对象。
void addNum(int val) 向数据流中加入整数 val 。
int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。

"""

# 方法一：使用有序映射维护区间
# 时间复杂度：
# addNum()：O(logn)
# getIntervals()：O(n)
# 空间复杂度：O(n)
from sortedcontainers import SortedDict
class SummaryRanges:

    def __init__(self):
        self.intervals = SortedDict()


    def addNum(self, val: int) -> None:
        intervals_ = self.intervals
        keys_ = self.intervals.keys()
        values_ = self.intervals.values()

        interval1 = intervals_.bisect_right(val)
        interval0 = (len(intervals_) if interval1 == 0 else interval1 - 1)
        #print('intervals_ before:', intervals_)
        #print('interval1:', interval1)
        #print('interval0:', interval0)

        if interval0 != len(intervals_) and keys_[interval0] <= val <= values_[interval0]:
            return 
        else:
            left_side = (interval0 != len(intervals_) and values_[interval0] + 1 == val)
            right_side = (interval1 != len(intervals_) and keys_[interval1] - 1 == val)
            if left_side and right_side:
                left, right = keys_[interval0], values_[interval1]
                intervals_.popitem(interval1)
                intervals_.popitem(interval0)              
                intervals_[left] = right
            elif left_side:
                intervals_[keys_[interval0]] += 1
            elif right_side:
                right = values_[interval1]
                intervals_.popitem(interval1)
                intervals_[val] = right
            else:
                intervals_[val] = val

        print('intervals_ after:', intervals_)

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals.items())


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


