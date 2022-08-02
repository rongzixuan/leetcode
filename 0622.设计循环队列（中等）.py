"""
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：
MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
 

示例：
MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4

提示：
所有的值都在 0 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。

"""

# 方法一：数组
# 时间复杂度：O(1)
# 空间复杂度：O(k)
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.head = 0  # 头节点
        self.tail = 0  # 尾节点
        self.k = k
        self.fullFlag = False  # 队列是否满

    def enQueue(self, value: int) -> bool:
        if not self.fullFlag:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.k
            if self.head % self.k == self.tail % self.k:
                self.fullFlag = True
            return True
        return False

    def deQueue(self) -> bool:
        if self.fullFlag or (not self.fullFlag and (self.tail % self.k) != (self.head % self.k)):
            self.queue[self.head] = -1
            self.head = (self.head + 1) % self.k
            if self.fullFlag:
                self.fullFlag = False
            return True
        return False

    def Front(self) -> int:
        return self.queue[self.head % self.k]

    def Rear(self) -> int:
        return self.queue[(self.tail - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.fullFlag == False and self.head == self.tail

    def isFull(self) -> bool:
        return self.fullFlag


# 方法二：数组
# 时间复杂度：O(1)
# 空间复杂度：O(k)
class MyCircularQueue:
    def __init__(self, k: int):
        self.front = self.rear = 0
        self.elements = [0] * (k + 1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % len(self.elements)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.elements)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.elements[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % len(self.elements)]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.elements) == self.front


# 方法三：链表
# 时间复杂度：O(1)
# 空间复杂度：O(k)
# ListNode为leetcode内部实现类
class MyCircularQueue:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.k = k
        self.count = 0  # 统计个数

    def enQueue(self, value: int) -> bool:
        if self.count < self.k:
            if self.head == None:
                self.head = self.tail = ListNode(value)
            else:
                self.tail.next = ListNode(value)
                self.tail = self.tail.next
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.count > 0:
            self.head = self.head.next
            self.count -= 1
            return True
        return False

    def Front(self) -> int:
        return self.head.val if self.head != None else -1

    def Rear(self) -> int:
        return self.tail.val if self.head != None else -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


