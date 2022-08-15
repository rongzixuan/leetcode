"""
设计实现双端队列。

实现 MyCircularDeque 类:
MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。
 
示例 1：
输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

输出
[null, true, true, true, false, 2, true, true, true, 4]

解释
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4

提示：
1 <= k <= 1000
0 <= value <= 1000
insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull  调用次数不大于 2000 次

"""

# 方法一：数组
class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [-1] * k  # 双端队列
        self.head = 0  # 头节点
        self.tail = 1 % k  # 尾节点
        self.k = k
        self.count = 0  # 元素个数

    def insertFront(self, value: int) -> bool:
        if self.count < self.k:
            self.deque[self.head] = value
            self.head = (self.head - 1 + self.k) % self.k
            self.count += 1
            #print(self.deque)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.count < self.k:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1 + self.k) % self.k
            self.count += 1
            #print(self.deque)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.count > 0:   
            self.head = (self.head + 1 + self.k) % self.k     
            self.deque[self.head] = -1                      
            self.count -= 1
            #print(self.deque)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.count > 0:
            self.tail = (self.tail - 1 + self.k) % self.k 
            self.deque[self.tail] = -1    
            self.count -= 1
            #print(self.deque)                     
            return True
        return False

    def getFront(self) -> int:
        if self.count > 0:
            return self.deque[(self.head + 1 + self.k) % self.k]
        return -1

    def getRear(self) -> int:
        if self.count > 0:
            return self.deque[(self.tail - 1 + self.k) % self.k]
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# 方法二：链表
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None  # 头节点
        self.tail = None  # 尾节点
        self.k = k
        self.count = 0  # 元素个数

    def insertFront(self, value: int) -> bool:
        if self.count < self.k:
            if self.head == None:
                self.head = self.tail = ListNode(value)
            else:
                tmp = ListNode(value)
                tmp.next = self.head
                self.head = tmp
            self.count += 1
            #print(self.head)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.count < self.k:
            if self.tail == None:
                self.tail = self.head = ListNode(value)
            else:
                self.tail.next = ListNode(value)
                self.tail = self.tail.next
            self.count += 1
            #print(self.head)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.count > 0:   
            if self.count == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next                    
            self.count -= 1
            #print(self.head)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.count > 0:
            if self.count == 1:
                self.head = self.tail = None
            else:
                tmp = self.head
                for _ in range(self.count - 2):
                    tmp = tmp.next
                tmp.next = None  
                self.tail = tmp
            self.count -= 1
            #print(self.head)                     
            return True
        return False

    def getFront(self) -> int:
        if self.count > 0:
            return self.head.val
        return -1

    def getRear(self) -> int:
        if self.count > 0:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# 方法三：链表
class Node:
    __slots__ = 'prev', 'next', 'val'

    def __init__(self, val):
        self.prev = self.next = None
        self.val = val

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

