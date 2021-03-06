"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

"""

class MedianFinder:


    # 方法一：优先队列（小根堆+大根堆）
    # 时间复杂度：
    # addNum()：O(logn)
    # findMedian()：O(1)
    # 空间复杂度：O(n)，堆的开销
    def __init__(self):
        self.minList = list() # 通过负数建立大根堆
        self.maxList = list() # 大根堆


    def addNum(self, num: int) -> None:
        minList = self.minList
        maxList = self.maxList

        if not minList or num <= -minList[0]:
            heapq.heappush(minList, -num)
            if len(minList) > len(maxList) + 1:
                heapq.heappush(maxList, -heapq.heappop(minList))
        else:
            heapq.heappush(maxList, num)
            if len(maxList) > len(minList):
                heapq.heappush(minList, -heapq.heappop(maxList))


    def findMedian(self) -> float:
        maxList = self.maxList
        minList = self.minList

        #print('1', minList, maxList)
        if len(maxList) == len(minList):
            #print('2', minList, maxList)
            return (-minList[0] + maxList[0]) / 2
        else:
            #print('3', minList, maxList)
            return -minList[0]


    # 方法二：
    # 时间复杂度：有序列表 + 双指针
    # addNum()：O(logn)
    # findMedian()：O(1)
    # 空间复杂度：O(n)， 队列的开销
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        from sortedcontainers import SortedList
        self.nums = SortedList()
        self.left = self.right = None
        self.left_value = self.right_value = None
    

    def addNum(self, num: int) -> None:
        nums = self.nums
        n = len(nums)
        nums.add(num)

        #print(self.left, self.right)
        if n == 0:
            self.left = self.right = 0
        else:
            if n & 1: # 奇数
                if num < self.left_value:
                    self.right += 1
                elif num >= self.right_value:
                    self.right += 1
            else: # 偶数
                if num < self.left_value:
                    self.left += 1
                elif self.left_value <= num < self.right_value:
                    self.left += 1
                elif num >= self.right_value:
                    self.left += 1
        
        self.left_value = nums[self.left]
        self.right_value = nums[self.right]


    def findMedian(self) -> float:
        nums = self.nums
        left_value, right_value = self.left_value, self.right_value
        return (left_value + right_value) / 2

    # 进阶1：计数排序 + 双指针
    # 进阶2：进阶排序 +双指针 + 小于0的数组 + 大于100的数组
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

